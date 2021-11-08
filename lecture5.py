import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import arange


def activity1(source_path):
    df = pd.read_csv(source_path)
    #print(df.head(20))

    total_profit_months = df[['month_number' , 'total_profit']]

    print(total_profit_months)
    plt.plot(total_profit_months['month_number'], total_profit_months['total_profit'])
    plt.xlabel('months')
    plt.ylabel('Total profit')
    plt.title('Total profits per Month')
    plt.xticks(np.arange(1,13,1))
    plt.yticks(np.arange(100000,500000+100000, 100000))
    plt.show()

def activity2(source_path):
    df = pd.read_csv(source_path)
    total_profit_months = df[['month_number' , 'total_profit']]
    plt.plot(total_profit_months['month_number'], total_profit_months['total_profit'],'ro--',mfc='k',linewidth=3 )

    plt.legend(["Profit data of last year"],loc = 4)
    plt.xlabel('months')
    plt.ylabel('Total profit')
    plt.title('Total profits per Month')

    plt.xticks(np.arange(1,13,1))
    plt.yticks(np.arange(100000,500000+100000, 100000))
    plt.show()

def activity3(source_path):

    df = pd.read_csv(source_path)
    months=df["month_number"]

    #facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer
    facecream=df['facecream']
    facewash=df['facewash']
    toothpaste = df['toothpaste']
    bathingsoap = df['bathingsoap']
    shampoo = df['shampoo']
    moisturizer = df['moisturizer']

    plt.plot(months, facecream,'o-')
    plt.plot(months, facewash,'o-')
    plt.plot(months, toothpaste,'o-')
    plt.plot(months, bathingsoap,'o-')
    plt.plot(months, shampoo,'o-')
    plt.plot(months, moisturizer,'o-')

    lengend_list = ["facecream Sales Data ","facewash Sales Data ","toothpaste Sales Data ",
                    "bathingsoap Sales Data ","shampoo Sales Data ","moisturizer Sales Data "]

    plt.legend(lengend_list)

    plt.xlabel("Month Number")
    plt.ylabel("Sales units in number")
    plt.show()


def activity4(source_path):

    df = pd.read_csv(source_path)
    months=df["month_number"]
    toothpaste = df['toothpaste']

    plt.scatter(months,toothpaste)
    plt.xticks(np.arange(1, 13, 1))
    plt.grid(linestyle= "--")

    plt.show()

def activity5(source_path):
    df = pd.read_csv(source_path)
    months = df["month_number"]
    facecream = df['facecream']
    facewash = df['facewash']

    #x_axis=np.arange(len(months))


    plt.bar(months-0.125-0.01, facecream,0.25)
    plt.bar(months+0.125+0.01, facewash,0.25)
    plt.xticks(np.arange(1, 13, 1))

    plt.xlabel("Month Number")
    plt.ylabel("Sales units in number")

    plt.legend(["Face Cream sales data ", "Face Wash sales data"], loc =2)
    plt.grid(linestyle= "--")
    plt.legend("Facewash and facecream sales data")
    plt.show()

def activity6(source_path):
    df = pd.read_csv(source_path)
    months = df["month_number"]
    bathingsoap = df['bathingsoap']



    plt.title("bathingsoap sales data")
    plt.xlabel("Month Number")
    plt.xticks(np.arange(1, 13, 1))
    plt.ylabel("Sales units in number")
    plt.grid(linestyle="--")

    plt.bar(months, bathingsoap,0.8)

    plt.show()



def activity7(source_path):
    df = pd.read_csv(source_path)
    months = df["month_number"]
    total_profit = df['total_profit']






    plt.title("Profit data")
    plt.xlabel("profit range in dollar")
    plt.ylabel("Actual Profit in dollar")

    arr=[150000,175000,200000, 225000,250000,300000,350000]

    plt.hist(total_profit,bins=arr)
    plt.show()


def activity8(source_path):
    df = pd.read_csv(source_path)

    total_year_profit = df['total_profit'].sum()

    facecream=df['facecream'].sum()
    facewash=df['facewash'].sum()
    toothpaste = df['toothpaste'].sum()
    bathingsoap = df['bathingsoap'].sum()
    shampoo = df['shampoo'].sum()
    moisturizer = df['moisturizer'].sum()

    slices= [facecream/total_year_profit,
             facewash/total_year_profit,
             toothpaste/total_year_profit,
             bathingsoap/total_year_profit,
             shampoo/total_year_profit,
             moisturizer/total_year_profit
             ]


    labels =["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]


    plt.pie(slices,labels=labels,autopct='%1.1f%%')

    plt.show()



def activity9(source_path):
    df = pd.read_csv(source_path)
    months = df["month_number"]
    bathingsoap = df['bathingsoap']
    facewash=df["facewash"]

    fig, ax = plt.subplots(2)

    ax[0].plot(months,bathingsoap,"ko-")
    ax[0].set_title("Sales data of Bathingsoap")

    ax[1].plot(months,facewash,"ro-")
    ax[1].set_title("Sales data of facewash")

    plt.show()


def activity10(source_path):
    df = pd.read_csv(source_path)
    months = df["month_number"]

    facecream=df['facecream']
    facewash=df['facewash']
    toothpaste = df['toothpaste']
    bathingsoap = df['bathingsoap']
    shampoo = df['shampoo']
    moisturizer = df['moisturizer']

    labels = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

    plt.stackplot(months,facecream,facewash,toothpaste, bathingsoap, shampoo, moisturizer)
    plt.legend(labels,loc =2 )
    plt.xticks(np.arange(1, 13, 1))
    plt.title("All product sales dat using stack plot")
    plt.xlabel("Month Number")
    plt.ylabel("Sales units in Number")

    plt.show()





















