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
        data: ['杭州','广州','深圳','上海','北京']
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
            data: [2330, 3532, 4969, 5673, 9570]
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
            data: [1229, 1259, 2118, 2568, 5174]
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
            data: [792, 683, 1338, 1756, 3523]
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
            data: [208, 247, 374, 596, 1147]
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
            data: [74, 82, 150, 202, 432]
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
            data: [71, 102, 145, 210, 379]
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
            data: [348, 513, 783, 1028, 1864]
        }
    ]
};