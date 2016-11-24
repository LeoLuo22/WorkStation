#include "led.h"
#include "delay.h"
#include "sys.h"
#include "usart.h"
#include "lcd.h"
#include "tsensor.h"


 int main(void)
 { 
	u16 adcx;
	float temp;
	float temperate;	 
	u8 t;
	 u8 i;
	u8 len;
	u16 times = 0;
	u16 time = 0;
	u8 flag = 0;
	delay_init();	    	 //延时函数初始化	  
	uart_init(9600);	 	//串口初始化为9600
	LED_Init();			 //初始化与LED连接的硬件接口
	
 	LCD_Init();
 	T_Adc_Init();		  		//ADC初始化	    
	POINT_COLOR=RED;//设置字体为红色 

	LCD_ShowString(60,50,200,16,16,"Mini STM32");	
	LCD_ShowString(60,70,200,16,16,"Temperature TEST");	
	LCD_ShowString(60,90,200,16,16,"ATOM@ALIENTEK");
	LCD_ShowString(60,110,200,16,16,"2014/3/9");	
	//显示提示信息											      
	POINT_COLOR=BLUE;//设置字体为蓝色
	LCD_ShowString(60,130,200,16,16,"TEMP_VAL:");	      
	LCD_ShowString(60,150,200,16,16,"TEMP_VOL:0.000V");	      
	LCD_ShowString(60,170,200,16,16,"TEMPERATE:00.00C");	
	
while(!flag)
{
if(USART_RX_STA&0x8000)
		{					   
			len=USART_RX_STA&0x3fff;//得到此次接收到的数据长度
			//time = USART_RX_STA;
			//printf("\r\n您发送的消息为:\r\n");
			for(t=0;t<len;t++)
			{
				u16 tmp =1;
				for(i = 0; i < (len - t - 1); i++){
					tmp = tmp * 10;
				}
				time = time + (USART_RX_BUF[t] - 48) * tmp;
				//printf("\r\nsta = %u\r\n", USART_RX_STA);
				//USART1->DR=USART_RX_BUF[t];
				//printf("\r\nBUF[%u] = %u\r\n",t, USART_RX_BUF[t] - 48);
				//printf("\r\nDR=%u\r\n", USART1->DR);
				while((USART1->SR&0X40)==0);//等待发送结束
			}
			printf("\r\n\r\n");//插入换行
			flag = 1;
			USART_RX_STA=0;
		}else
		{
			times++;
			if(times%200==0)printf("请设置时间间隔\r\n");  
			if(times%30==0)LED0=!LED0;//闪烁LED,提示系统正在运行.
			delay_ms(10);   
		}
	}
	printf("\r\n你设置的时间间隔为：%ums\r\n",time);
	while(1)
	{
		adcx=T_Get_Adc_Average(ADC_CH_TEMP,10);
		LCD_ShowxNum(132,130,adcx,4,16,0);//显示ADC的值
		temp=(float)adcx*(3.3/4096);
		temperate=temp;//保存温度传感器的电压值
		adcx=temp;
		LCD_ShowxNum(132,150,adcx,1,16,0);     		//显示电压值整数部分
		temp-=(u8)temp;				    			//减掉整数部分		  
		LCD_ShowxNum(148,150,temp*1000,3,16,0X80);	//显示电压小数部分
 		temperate=(1.43-temperate)/0.0043+25;		//计算出当前温度值	 
		LCD_ShowxNum(140,170,(u8)temperate,2,16,0); //显示温度整数部分
		printf("\r\n当前的温度为：\r\n");
		printf("%f",temperate);
		temperate-=(u8)temperate;	  
		LCD_ShowxNum(164,170,temperate*100,2,16,0X80);//显示温度小数部分
		LED0=!LED0;
		//printf("%u", time);
		delay_ms(time * 10);
	}										    
}	
