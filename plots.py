import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from get_data import *
from volatility import *
from black_scholes_pricing import *

def plot_vs_S(K,T,r,sig,q=0):
    S = np.linspace(K - 0.25*K, K+0.25*K,100)
    
    plt.figure(1,figsize=(7, 4))
    bm = BlackScholes(S,K,T,r,sig)
        
    plt.plot(S,bm._call(),linewidth=2,label='Call')
    plt.plot(S,bm._put(),linestyle='--',linewidth=2,label='Put')
    
    plt.axvline(x=K, color='black', linestyle=':', label='Strike')
    plt.xlabel('$S$')
    plt.ylabel('Option Price')
    plt.title('Option Price as a function of the underlying')
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.legend(loc='upper left',frameon=False)
    plt.tight_layout()
    return
    

def plot_vs_T(S,K,r,sig,q=0):
    T = np.linspace(0.01,2,100)
    bm = BlackScholes(S,K,T,r,sig)
    
    plt.figure(2,figsize=(7, 4))

    plt.plot(T,bm._call())
    plt.plot(T,bm._put())  
    
    plt.xlabel('$T$')
    plt.ylabel('Option Price')
    plt.title('Option Price as a function of time to expiration')
    plt.legend(loc='upper left',frameon=False)
    plt.grid(True, linestyle=':', alpha=0.7)
    return


def plot_vs_sig(S,K,T,r,q=0):
    sig = np.linspace(0.0001,1.01,100)
    
    plt.figure(3,figsize=(7, 4))

    bm = BlackScholes(S,K,T,r,sig)
    plt.plot(sig,bm._call(),label='Call',linewidth=2)
    plt.plot(sig,bm._put(),label='Put',linestyle='--',linewidth=2) 
    
    # Add vertical line for at-the-money volatility
    #atm_vol = 0.2  # You can adjust this or calculate it based on market data
    #plt.axvline(x=atm_vol, color='green', linestyle='--', label='Typical ATM Volatility')
    
    # Improve labels and title
    plt.xlabel('$\sigma$')
    plt.ylabel('Option Price')
    plt.title('Option Price as a function of Volatility')
    
    # Add gridlines for better readability
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper left',frameon=False)
    plt.tight_layout()
    return


def plot_ST_contour(K,r,sig):
    S = np.linspace(K - 0.25*K, K+0.25*K,100)
    T = np.linspace(0.01,2,100)
    
    call = np.zeros((len(S),len(T)))
    for i in range(len(S)):
        for j in range(len(T)):
            bm = BlackScholes(S[i],K,T[j],r,sig)
            call[i,j] = bm._call()
            
    S,T = np.meshgrid(S,T)
    fig =  plt.figure(4,(7,4))
    surface = plt.contourf(S,T,call, cmap='Blues')
    plt.xlabel(r'$S$')
    plt.ylabel(r'$T$')
    #ax.set_zlabel('Option Price')  
    fig.tight_layout()
    #plt.colorbar(surface)
    cbar = fig.colorbar(surface)
    cbar.set_label('option Price')
    plt.show()       
    return