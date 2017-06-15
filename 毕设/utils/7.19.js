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
        data: ['杭州','广州','深圳','上海','北京']
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
            data: [45.15, 43.62, 43.15, 40.38, 41.20]
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
            data: [29.10, 23.67, 27.26, 27.61, 28.20]
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
            data: [7.64, 8.56, 7.62, 9.37, 9.18]
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
            data: [2.72, 2.84, 3.06, 3.18, 3.46]
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
            data: [2.43, 3.53, 2.95, 3.30, 3.03]
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
            data: [12.78, 17.78, 15.95, 16.16, 14.92]
        }
    ]
};