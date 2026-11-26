# The actual endpoint kernel on fixed nonreal bands

Private written proof, 16 November 2026.

The periodic inhomogeneous recurrence determines an explicit leading
term for the original kernel divided by its physical relation. The
estimate is uniform on every fixed band separated from the real axis,
for all bounded complex microscopic parameters, including the physical
imaginary marks. It also determines the original first spectral normal.
This is an outer approximation to the actual canonical source. It is
not a homogeneous representative or a sharp Green boundary estimate.

## 1. Statement and original source

Put
\[
 h=N^{-1},\quad N\ge2,\quad c_0=2\cos(\pi h),\quad
 c_N(x)=2\cos(2\pi x+\pi h),\quad w_N(\alpha)=2\cosh(\alpha h),
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 p_N(x)=P_N(c_N(x))=4\sin^2(\pi Nx),\qquad
 p(\alpha)=P_N(w_N(\alpha))=4\cosh^2(\alpha/2).
 \tag{1}
\]
Here \(T_N\) in (1) is the Chebyshev polynomial. The original
ordinary kernel is
\[
 K_N(w,C)=\sum_{j=0}^{N-1}e_j(w)e_j(C),\qquad
 e_j(C)=\frac{\prod_{a<j}(c_a-C)}
                  {\prod_{a=1}^j(2\sin(a\pi/N))^2},
 \quad c_a=2\cos((2a+1)\pi/N).
 \tag{2}
\]
Define, away from the real axis,
\[
 r_N(x,\alpha)=\frac{N^2K_N(w_N(\alpha),c_N(x))}{p_N(x)},
 \qquad
 r_0(x,\alpha)=-\frac{\cosh^2(\alpha/2)}{\pi^2+\alpha^2}
                                      \csc^2(\pi x).
 \tag{3}
\]
The apparent singularities of \(r_0\) at \(\alpha=\pm i\pi\)
are removable: its numerator has a double zero there and its
denominator a simple zero. Thus both functions in (3) are entire
in \(\alpha\).

For \(0<H_0<H_1<\infty\), write
\[
 \mathcal B(H_0,H_1)=
       \{x\in\mathbb C:H_0\le |\Im x|\le H_1\}.
 \tag{4}
\]
All functions being estimated are period one in \(x\), so no
restriction on its real part is needed.

**Theorem.** Fix \(A<\infty\), \(0<H_0<H_1<\infty\), and
nonnegative integers \(a,b\). There are \(C,N_0\), depending
only on these fixed data, such that
\[
 \boxed{\quad
 \sup_{\substack{|\alpha|\le A\\x\in\mathcal B(H_0,H_1)}}
 \left|\partial_\alpha^a\partial_x^b(r_N-r_0)(x,\alpha)\right|
                         \le \frac C N\qquad(N\ge N_0).
 \quad}                                                     \tag{5}
\]
In particular, (5) is an absolute estimate through every odd
imaginary physical mark; no division by \(p(\alpha)\) remains
in the statement.

The original first spectral normal has the corresponding limit
\[
 \boxed{\quad
 \frac{N}{p_N(x)}\partial_C K_N(w_N(\alpha),c_N(x))
 =\frac{i\,\operatorname{sgn}(\Im x)}{2\sin(2\pi x)}
                                      r_0(x,\alpha)+O(N^{-1}).
 \quad}                                                     \tag{6}
\]
The error is uniform on (4) and bounded parameter disks. Every
fixed \(x\)- or \(\alpha\)-derivative has the same error bound
on buffered bands and parameter disks.

## 2. Balanced forced recurrence

Use the ordinary operator and its exact source from the monodromy
note:
\[
 \mathscr J_NF=(c_0+A_N+B_N)F-A_NF(x+h)-B_NF(x-h),
\]
\[
 A_N(x)=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\qquad
 B_N(x)=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}},\qquad
 s_z=2\sin(\pi z/N),
\]
\[
 (w_N-\mathscr J_N)K_N(w_N,c_N(x))
             =\frac{p(\alpha)p_N(x)}{N^4(c_N(x)-c_0)}.
 \tag{7}
\]
The function \(p_N\) is \(h\)-periodic and commutes with this
ordinary operator. Consequently the actual function in (3)
satisfies
\[
        (w_N-\mathscr J_N)r_N
                  =\frac{p(\alpha)h^2}{c_N(x)-c_0}.
 \tag{8}
\]
All coefficients and denominators in (7)--(8) are regular on a
fixed nonreal band for sufficiently large \(N\). The normal
equations are obtained by ordinary differentiation there.

For any scalar \(f\), set
\[
 X_f(x)=\binom{f(x)}{h^{-1}(f(x)-f(x-h))},\qquad
 q_N=B_N/A_N,\quad d_N=(c_0-w_N)/A_N,
\]
\[
 \mathcal T_N=
       \begin{pmatrix}1+d_N&h q_N\\d_N/h&q_N\end{pmatrix}.
 \tag{9}
\]
Solving (8) for the forward value gives the exact forced equation
\[
 X_{r_N}(x+h)=\mathcal T_N(x,\alpha)X_{r_N}(x)
                                      +\beta_N(x,\alpha),
 \qquad
 \beta_N=\frac{p(\alpha)}{A_N(c_N-c_0)}\binom{h^2}{h}.
 \tag{10}
\]
In particular the source sign in (10) is positive; its limiting
second entry below is negative because \(c_N-c_0\) tends to
\(-4\sin^2(\pi x)\).

On every buffered band, uniformly for bounded \(\alpha\), direct
Taylor expansion gives
\[
 A_N=\tan^2(\pi x)+O(h),\qquad
 q_N=1-h\pi\{3\cot(\pi x)+\tan(\pi x)\}+O(h^2),
\]
\[
 d_N=-h^2(\pi^2+\alpha^2)\cot^2(\pi x)+O(h^3),
\]
\[
 \mathcal T_N=I+h\mathcal B_\alpha+O(h^2),\qquad
 \mathcal B_\alpha=
 \begin{pmatrix}
 0&1\\
 -(\pi^2+\alpha^2)\cot^2(\pi x)&
       -\pi\{3\cot(\pi x)+\tan(\pi x)\}
 \end{pmatrix},
\]
\[
 \beta_N=h\binom0{\displaystyle
       -\cosh^2(\alpha/2)\frac{\cos^2(\pi x)}{\sin^4(\pi x)}}
                                                           +O(h^2).
 \tag{11}
\]
For the second expansion one may take the logarithm of the exact
ratio
\[
 q_N=\frac{\sin^4(\pi x)}{\sin^4(\pi(x+h))}
                         \frac{\sin(2\pi(x+h))}{\sin(2\pi x)}.
\]
Every displayed error and every fixed derivative is uniform after
reserving a larger band and parameter disk.

The limiting scalar differential operator is
\[
 \mathcal L_\alpha f=f''+
       \pi(3\cot(\pi x)+\tan(\pi x))f'
                   +(\pi^2+\alpha^2)\cot^2(\pi x)f.
 \tag{12}
\]
Direct differentiation, including the derivative of \(\cot\), gives
\[
 \mathcal L_\alpha[\csc^2(\pi x)]
             =(\pi^2+\alpha^2)
                           \frac{\cos^2(\pi x)}{\sin^4(\pi x)}.
 \tag{13}
\]
Thus \(r_0\) solves precisely the limiting forced equation in
(11). It is period one. Taylor expansion of its balanced state,
using (11)--(13), proves
\[
 \varepsilon_N(x):=
 X_{r_0}(x+h)-\mathcal T_N(x)X_{r_0}(x)-\beta_N(x)
                                                   =O(h^2).
 \tag{14}
\]
This is a residual of the explicitly given function, not an
assumed approximation to an unknown selected homogeneous mode.

## 3. Period inversion with its norm and parameter removal

Let \(\mathcal M_N(x,\alpha)\) be the ordered \(N\)-step product
of the matrices in (9). The balanced state is obtained from the
two-value state in the monodromy note by a constant invertible
change of basis. Their period matrices are therefore similar.
In particular its exact determinant and trace are
\[
 \det\mathcal M_N=1,\qquad
 \operatorname{tr}\mathcal M_N
                      =2+p(\alpha)\cot^2(\pi Nx),
\]
\[
       \det(I-\mathcal M_N)
                      =-p(\alpha)\cot^2(\pi Nx).
 \tag{15}
\]
Although the balancing change itself depends on \(N\), the norm
of the balanced product is bounded directly: (11) gives
\(\|\mathcal T_N\|\le1+Ch\) at every point of the horizontal
orbit. Hence all its partial products, of length at most \(N\),
have norm at most \(e^C\). This is the norm estimate needed in
addition to the algebraic determinant identity.

First restrict \(\alpha\) to a compact set where
\(|p(\alpha)|\ge c>0\). On (4),
\(\cot^2(\pi Nx)=-1+O(e^{-2\pi NH_0})\) uniformly in
\(\Re x\). Formula (15) and the bounded entries of
\(\mathcal M_N\) give
\[
                       \|(I-\mathcal M_N)^{-1}\|\le C.
 \tag{16}
\]
Set \(E_N=X_{r_N}-X_{r_0}\). Equations (10) and (14) imply
\(E_N(x+h)=\mathcal T_N(x)E_N(x)-\varepsilon_N(x)\).
Both states are exactly period one, so iteration through the
actual period gives
\[
 (I-\mathcal M_N)E_N(x)
 =-\sum_{l=0}^{N-1}
       \mathcal T_N(x+(N-1)h)\cdots
       \mathcal T_N(x+(l+1)h)\varepsilon_N(x+lh).
 \tag{17}
\]
An empty product is the identity. The right side is \(O(Nh^2)=O(h)\).
Equations (16)--(17) prove the uniform \(O(h)\) bound for the
whole balanced error state on this parameter set.

There is no parameter-unit restriction in the theorem. Given
\(A\), choose a fixed \(R>A\) which is not an odd multiple of
\(\pi\). The circle \(|\alpha|=R\) contains no zero of
\(p(\alpha)\), so the preceding estimate holds uniformly on
that circle. For each \(x\) the actual error state is entire
in \(\alpha\); the maximum principle extends the same bound
to its disk. Taking a still larger circle gives Cauchy estimates
for every fixed parameter derivative. Repeating the argument on
a band with smaller positive lower height and larger upper height
gives Cauchy estimates for every fixed \(x\)-derivative. This
proves (5), including all exceptional odd imaginary marks.

## 4. The original spectral normal and the scope of the estimate

The identity \(K_N=p_Nr_N/N^2\) gives exactly
\[
 \frac{N}{p_N(x)}\partial_CK_N(w_N,c_N(x))
   =\frac{2\pi\cot(\pi Nx)r_N(x)+h\partial_xr_N(x)}
                                                   {c_N'(x)}.
 \tag{18}
\]
On a fixed nonreal band, \(c_N'\) is uniformly bounded away
from zero and converges to \(-4\pi\sin(2\pi x)\).
Also \(\cot(\pi Nx)\) converges to
\(-i\operatorname{sgn}(\Im x)\) exponentially. Substituting
(5) into (18) proves (6) with the stated derivative bounds.
Thus the estimate keeps the original first normal, rather than
reconstructing it from physical values or discarding a high
Newton sector.

For real \(|\alpha|\le A\), the leading factors in (3) and
(6) are uniform units on (4), modulo the period in \(\Re x\).
Consequently there are constants \(c,C>0\) such that, for all
large \(N\),
\[
 cN^{-2}e^{2\pi N|\Im x|}
 \le |K_N(w_N(\alpha),c_N(x))|
 \le CN^{-2}e^{2\pi N|\Im x|},
\]
\[
 cN^{-1}e^{2\pi N|\Im x|}
 \le |\partial_CK_N(w_N(\alpha),c_N(x))|
 \le CN^{-1}e^{2\pi N|\Im x|}.
 \tag{19}
\]
These are pointwise canonical-kernel bounds on fixed nonreal
bands. At complex physical parameters the leading term can
vanish; only the absolute estimates (5)--(6) are asserted there.

Neither the band height nor the period inverse in this proof is
uniform as the band approaches the physical line. The argument
does not replace the actual kernel by a homogeneous solution.
In particular the leading term describes the exponentially large
canonical source away from that line. A moderate homogeneous
contribution there would be exponentially smaller after division
by \(p_N\), and is not determined by the power error in (5).
The actual fractional-grid boundary packet and the baseline
defect in the sharp Green budget remain separate obligations.
No \(J_*\) comparison, current bound, or filled-leaf scalar seed
follows from this theorem.

## 5. Coverage and complete direct sources

The cyclic affine inverse and the full-Hermite half-plane
representatives are archived constructions. The explicit top
Fourier coefficient also gives a previous full-strip norm
obstruction. The additional result here is the uniform pointwise
asymptotic of the actual periodic forced kernel, with its leading
coefficient, all bounded complex parameters and its original
spectral normal. A targeted coverage search found no such
canonical normalized-kernel asymptotic.

The following complete direct sources were read at these pins,
and the used implications checked:

* [Exact ordinary source and period monodromy](research_unturned_endpoint_exact_period_monodromy.md),
  SHA256 d082d1ef103c7c200340e36c6a79442ee658bf2582549cd399acb0384391a7a1.
* [The sharp Green budget and its retained fractional boundary](research_partial_endpoint_green_boundary_budget.md),
  SHA256 a1bbfaa8f64abca96d2b97078a9d87fbc60877b4f4791612b1e8e2d822be286e.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts remain
unchanged.
