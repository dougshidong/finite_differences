#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import sys, math
from cmath import *

def complex_step(f,x,h):
	return f(complex(x,h)).imag/h
def forward_fd(f,x,h):
	return (f(x+h) - f(x))/h
def central_fd(f,x,h):
	return (f(x+h) - f(x-h))/(2.0*h)

def function(x):
	return np.sin(x)
	#return 1e-5*x
	#return x*x*x;

x_0 = 1
n = 17
error_cs = np.empty(n)
error_fd = np.empty(n)
error_cd = np.empty(n)
step_sizes = np.empty(n)

dfdx_exact = np.cos(x_0)
#dfdx_exact = 3*x_0*x_0
for i in range(n):
	h = 10**(-i)
	#h = 10**(i)
	step_sizes[i] = i
	
	dfdx = forward_fd(function,x_0,h)
	error_fd[i] = abs(dfdx - dfdx_exact)#/dfdx_exact

	dfdx = central_fd(function,x_0,h)
	error_cd[i] = abs(dfdx - dfdx_exact)#/dfdx_exact
	
	dfdx = complex_step(function,x_0,h)
	error_cs[i] = abs(dfdx - dfdx_exact)#/dfdx_exact+1e-16

print(error_fd)
print(error_cd)
pdfName = './finite_difference_trunc.pdf'
pp=PdfPages(pdfName)
plt.figure(figsize=(8,4))
plt.title('Finite-Difference Error')
plt.semilogy(step_sizes[:5], error_fd[:5], '-o',label='Forward FD')
plt.semilogy(step_sizes[:5], error_cd[:5], '-o',label='Central FD')
#plt.semilogy(step_sizes, error_cs, '-o',label='Complex Step')
plt.legend()
plt.xlabel(r'$-log_{10}(h)$')
plt.ylabel(r'Relative Error')
plt.grid(b=True, which='major', color='black', linestyle='-',alpha=0.2)
plt.tight_layout()
pp.savefig(bbx_inches='tight')
pp.close()

pdfName = './finite_difference_round.pdf'
pp=PdfPages(pdfName)
plt.figure(figsize=(8,4))
plt.title('Finite-Difference Error')
plt.semilogy(step_sizes, error_fd, '-o',label='Forward FD')
plt.semilogy(step_sizes, error_cd, '-o',label='Central FD')
#plt.semilogy(step_sizes, error_cs, '-o',label='Complex Step')
plt.legend()
plt.xlabel(r'$-log_{10}(h)$')
plt.ylabel(r'Relative Error')
plt.grid(b=True, which='major', color='black', linestyle='-',alpha=0.2)
plt.tight_layout()
pp.savefig(bbx_inches='tight')
pp.close()

pdfName = './finite_difference_complexstep.pdf'
pp=PdfPages(pdfName)
plt.figure(figsize=(8,4))
plt.title('Finite-Difference Error')
plt.semilogy(step_sizes, error_fd, '-o',label='Forward FD')
plt.semilogy(step_sizes, error_cd, '-o',label='Central FD')
plt.semilogy(step_sizes, error_cs, '-o',label='Complex Step')
plt.legend()
plt.xlabel(r'$-log_{10}(h)$')
plt.ylabel(r'Relative Error')
plt.grid(b=True, which='major', color='black', linestyle='-',alpha=0.2)
plt.tight_layout()
pp.savefig(bbx_inches='tight')
pp.close()
plt.savefig('./allfd.png',bbox_inches='tight')
