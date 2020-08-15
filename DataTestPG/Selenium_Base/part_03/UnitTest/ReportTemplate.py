# encoding: utf-8

def htmlTemplate(trData):
    htmlStr = u'''<!DOCTYPE html>
    <html lang="en">
        <head>
    <title>单元测试报告</title>
    <style>
        body{
            width:80% ;
            margin: 40px auto ;
            font-weight: bold;
            font-family: 'trebuchet MS', 'Lucida sans', Simsun;
            font-size: 18px;
            color:  #000;
        }
        table{
            * border-collapse:collapse;
            border-spacing:0;
            width: 100%;
        }
        .tableStyle {
            /* border: solid #ggg 1px;*/
            border-style:outset;
            border-width: 2px;
            border-color: blue;
        }
        .tableStyle tr:hover{
            background:rgb(173,216,230);
        }
        .tableStyle td,.tableStyle th{
            border-left: solid 1px rgb(146,208,80);
            border-top: 1px solid rgb(146,208,80);
            padding:15px;
            text-align:center;
        }
        .tableStyle th {
            padding: 15px;
            background-color:rgb(146,208,80);
            background-image: -webkit-gradient(linear, left top, left bottom, from(#92D050), to(#A2D668));
            
        }
    </style>
</head>
<body>
    <center><h1>测试报告</h1></center>
    <br>
    <table class="tableStyle">
        <thead>
        <tr>
            <th>Search Words</th>
            <th>Assert Words</th>
            <th>Start Time</th>
            <th>Waste Time</th>
            <th>State</th>
        </tr>
        </thead>'''
    endStr = u'''
            </table>
            </body>
            </html>'''

    html = htmlStr + trData + endStr
    print(html)
    with open('/Users/cp/PycharmProjects/DataTestPG/Selenium_Base/part_03/UnitTest/hemlTemplate.html', 'w')as fp:
        fp.write(html.encode('gbk'))
