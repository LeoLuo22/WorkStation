app.title = '堆叠条形图';

option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data: ['未融资', '天使轮','A轮','B轮','C轮', 'D轮及以上', '上市公司']
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
            name: '未融资',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: [3095, 1670, 1333, 1119, 1027]
        },
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
            data: [625, 303, 333, 210, 183]
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
            data: [319, 176, 174, 106, 95]
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
            data: [111, 56, 57, 22, 18]
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
            data: [33, 30, 19, 8, 12]
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
            data: [38, 26, 14, 16, 19]
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
            data: [235, 194, 142, 87, 65]
        }
    ]
};