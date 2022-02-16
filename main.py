import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# ctrl+dで同じやつを選択
# sideberでサイドバーを作れる
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# DisplayInteractiveWidgets
# text = st.text_input('あなたが趣味を教えてください.')
# condition = st.slider('あなたの今の調子は?',0,10,5)

# 'あなたの趣味:',text
# 'コンディション:',condition

# if st.checkbox('Show Image'):
#     img=Image.open('92f4938b0a15322690ac28c8f2833928.jpg')
#     # use_column_width=Trueで幅を合わせる
#     st.image(img, caption='ハリネズミ',use_column_width=True)


# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# # プロットする API Display charts
# st.map(df)


# どちらでも同じ表が表示されるがdataframeは引数が指定できる
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
# st.table(df.style.highlight_max(axis=0))

# マジックコマンド
# """文字列の書き方

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """
# 遊んでみた
# st.balloons()
# with st.spinner('Wait for it...'):
#     st.success('Done!')




