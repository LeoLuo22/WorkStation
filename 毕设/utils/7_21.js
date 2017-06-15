app.title = '堆叠条形图';

option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data: ['天使轮','A轮','B轮','C轮', 'D轮及以上', '上市公司']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis:  {
        type: 'value'
    },
    yAxis: {
        type: 'category',
        data: ['成都', '武汉', '南京', '西安', '长沙']
    },
    series: [
        {
            name: '天使轮',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [45.92, 38.60, 45.06, 46.77, 46.68]
        },
        {
            name: 'A轮',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [23.44, 22.42, 23.55, 23.61, 24.23]
        },
        {
            name: 'B轮',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [8.16, 7.13, 7.71, 4.90, 4.59]
        },
        {
            name: 'C轮',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [2.42, 3.82, 2.57, 1.78, 3.06]
        },
        
        {
            name: 'D轮及以上',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [2.79, 3.31, 1.89, 3.56, 4.85]
        },
        {
            name: '上市公司',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [17.27, 24.71, 19.22, 19.38, 16.58]
        }
    ]
};