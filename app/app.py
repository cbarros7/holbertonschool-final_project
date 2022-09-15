
import joblib
import numpy as np
import pandas as pd
import streamlit as st


APP_FILE = "app.py"
MODEL_JOBLIB_FILE = "model.joblib"


def main():
    """This function runs/ orchestrates the Machine Learning App Registry"""
    st.markdown(
        """
# Machine Learning App 

The main objective of this app is building a customer segmentation based on credit card 
payments behavior during the last six months to define marketing strategies. 
You can find the source code for this project in the following [Github repository](https://github.com/cbarros7/holbertonschool-final_project).
"""
    )

    html_temp = """
    <div style="text-align: right"> <strong> Author: </strong> <a href=https://www.linkedin.com/in/carlosbarros7/ target="_blank">Carlos Barros</a>  </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown('## Dataset')
    if st.checkbox('Show sample data'):
        st.write(show_data)

    customer_predictor()


def customer_predictor():
    """## Customer predictor

    A user may have to input data about the customer's finances to predict which cluster he belongs to. 
    """
    st.markdown("## Customer segmentation model based on credit behavior")

    balance = st.number_input("Balance")
    purchases = st.number_input("Purchases")
    cash_advance = st.number_input("Cash Advance")
    credit_limit = st.number_input("Credit Limit")
    payments = st.number_input("Payments")
    prediction = 0

    if st.button("Predict"):
        model = joblib.load(MODEL_JOBLIB_FILE)
        features = [balance, purchases, cash_advance, credit_limit, payments]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        st.balloons()
        st.success(f"The client belongs to the cluster: {prediction[0]:.0f}")
        if(prediction[0] == 0):
            st.markdown("""
                        These kinds of customers pay a minimum amount in advance and their payment is proportional to the 
                        movement of their purchases, this means that they are good customers **paying the debts**  :hand: they incur 
                        with their credit cards. 
                        """)
        if(prediction[0] == 1):
            st.markdown("""
                        In this group are presented the customers who pay the **most in advance before** :ok_hand: the loan starts with 
                        a balanced balance statement because their purchases are minimal compared to the other groups, 
                        also it is the **second-best paying**.  :hand:
                        """)
        if(prediction[0] == 2):
            st.markdown("""
                        Customers in this cluster pay the minimum amount in advance, however, it is the **group that buys the most**:gift:  :sunglasses:, 
                        and it is also the **group that pays the most** :moneybag:. In other words, these types of customers are quite 
                        active regarding the number of purchases they make with their credit cards. 
                        """)
        if(prediction[0] == 3):
            st.markdown("""These clients are the ones with the highest balance status, in addition to that, 
                        they are the second group that pays the most in advance before starting their credit. 
                        However, they are the customers who make the **least purchases**  :sleepy: and following the same idea, 
                        they are the seconds when it comes to making payments on the debt with their credit card. This 
                        makes sense since they have an amount of the loan provided in advance. It can be concluded that 
                        they are **conservative** and **meticulous** customers when buying.    :expressionless:""")
        if(prediction[0] == 4):
            st.markdown("""
                        This group of customers has **low-frequency usage**  :sleeping: of their credit cards since it is the second group that 
                        purchases the least, in addition to that, they are customers who pay well in proportion to 
                        their purchases. As for the advance payment before starting the loan, it is minimal compared to the other groups. 
                        """)


@st.cache
def load_data():
    data = pd.read_csv('final_data.csv')
    data = data.drop(['Unnamed: 0'], axis=1)
    data = data.sort_index(axis=1)
    return data


show_data = load_data()

if __name__ == "__main__":
    main()
