import pandas as pd
import numpy as np

pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')

# def apply_links(x):
#   x = "<a href='rdp://"+x+">"+x+"</a>"
#   return x

np.random.seed(6182018)
demo_df = pd.DataFrame({'date': np.random.choice(pd.date_range('2018-01-01', '2018-06-18', freq='D'), 50),
                        'analysis_tool': np.random.choice(['pandas', 'r', 'julia', 'sas', 'stata', 'spss'],50),              
                        'database': np.random.choice(['postgres', 'mysql', 'sqlite', 'oracle', 'sql server', 'db2'],50), 
                        'os': np.random.choice(['windows 10', 'ubuntu', 'mac os', 'android', 'ios', 'windows 7', 'debian'],50), 
                        'num1': np.random.randn(50)*100,
                        'num2': np.random.uniform(0,1,50),                   
                        'num3': np.random.randint(100, size=50),
                        'bool': np.random.choice([True, False], 50)
                       },
                        columns=['date', 'analysis_tool', 'num1', 'database', 'num2', 'os', 'num3', 'bool']
          )

demo_df['os'] = demo_df['os'].apply(lambda x: f'<a href="rdp://{x}">{x}</a>')
print(demo_df.head(10))


html_string = '''
<html>
  <head><title>MCU</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    <div class="row">
    {table1}
    {table2}
    {table3}
    </div>
  </body>
</html>.
'''

# OUTPUT AN HTML FILE

with open("myhtml.html", 'w') as f:
    f.write(html_string.format(table1=demo_df.to_html(classes='column', escape=False),table2=demo_df.to_html(classes='column', escape=False),table3=demo_df.to_html(classes='column', escape=False)))
    # f.write('<link rel="stylesheet" type="text/css" href="df_style.css"/>'
    #         +'<center>' 
    #         +'<h1> MCU </h1><br><hr>'
    #         +'<div class="row">'
    #         +'<div class="column">' + demo_df.to_html(index=False,border=2,justify="center") + '<be><hr>'
    #         +'<div class="column">' + demo_df.to_html(index=False,border=2,justify="center") + '<br><hr>'
    #         +'<div class="column">' + demo_df.to_html(index=False,border=2,justify="center") + '<br><hr>'
    #         +'</center>')

# with open('myhtml.html', 'w') as f:
#     f.write(html_string.format(table=demo_df.to_html(classes='mystyle')))