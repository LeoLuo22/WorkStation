option = {
    title: {
        text: '互联网工资年限与对应年薪',
        subtext: '数据来源：拉勾网'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['产品','市场与销售', '技术', '职能', '设计', '运营', '金融']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['1年以下', '1-3年', '3-5年', '5-10年', '10年以上']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} K'
        }
    },
    series: [
        {
            name:'产品',
            type:'line',
            data:[82, 170, 222, 301, 399],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'市场与销售',
            type:'line',
            data:[75, 119, 150, 230, 349],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'技术',
            type:'line',
            data:[84, 168, 210, 303, 439],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'职能',
            type:'line',
            data:[50, 75, 126, 200, 353],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'设计',
            type:'line',
            data:[75, 118, 172, 233, 380],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'运营',
            type:'line',
            data:[52, 101, 152, 275, 412],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'金融',
            type:'line',
            data:[90, 172, 221, 323, 441],
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ]
            }
        },
        
    ]
};
