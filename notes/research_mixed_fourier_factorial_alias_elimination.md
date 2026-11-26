# Removing the two outgoing aliases at fixed level

Research deduction, 7 November 2026. For the exact low-index source,
the global factorial cardinal chart permits both outgoing horizontal
aliases to be sent to infinite height. The finite-level correction
in the marked factorial is essential at odd levels. The resulting
identity consists of the complete main path and one absolutely
convergent, signed vertical boundary current.

All limits below are taken with \(N\) fixed. This is an exact
reorganization of the source, not an estimate at its geometric
exponential rate. In particular the remaining vertical current has
an interval with no Fourier decay.

## 1. Exact factorial behavior at infinite height

Use the specified negative-root factorial
\[
 \Pi_N(z)=G_N(Nz)
       \exp\!\left\{\frac{\pi i}{2}[N(z-z^2)-z]\right\},
 \qquad N\ge2,
 \qquad
 \gamma_N=\frac N{12}-\frac14+\frac1{12N}.
 \tag{1}
\]
Here \(G_N\) is the original convergent Gamma product. The exact
formula in [the cyclotomic factorial proof](research_exact_cyclotomic_factorial.md),
equations (7)--(9), gives, for \(\Im z<0\),
\[
 \Pi_N(z)=\sqrt N\,e^{i\pi\gamma_N}e^{\mathcal E_N(z)}.
 \tag{2}
\]
Writing \(w=e^{-2\pi iz}\), its specified remainder is
\[
 \begin{split}
 \mathcal E_N(z)={}&z\Log(1-w^N)
   -\frac1N\sum_{k=0}^{N-1}k\Log(1-we^{2\pi ik/N})
   +\frac{i}{2\pi N}\operatorname{Li}_2(w^N),\\
 |\mathcal E_N(z)|\le{}&
 \left(|z|+\frac1{2\pi N}\right)\frac{|w|^N}{1-|w|^N}
 +\frac{N-1}{2}\frac{|w|}{1-|w|}.
 \end{split}
 \tag{3}
\]
The logarithms and dilogarithm are their disk series. Thus (2)
has the normalization of the actual Gamma product; it is not a
solution of a recurrence with an undetermined periodic factor.

For \(x\) in any fixed bounded real interval and \(H\to+\infty\),
\[
 \Pi_N(x-iH)=\sqrt N\,e^{i\pi\gamma_N}
       \left(1+O_N((1+H)e^{-2\pi H})\right),
 \tag{4}
\]
uniformly in \(x\). The original Gamma product also gives
\(G_N(\overline z)=\overline{G_N(z)}\). Consequently its marked
factorial satisfies the exact reflection identity
\[
 \Pi_N(z)=e^{\,i\pi[N(z-z^2)-z]}\,
                        \overline{\Pi_N(\overline z)}.
 \tag{5}
\]
It is valid on either open half-plane, where the factors are
nonzero. Applying (4) to the conjugate point proves
\[
 \Pi_N(x+iH)=\sqrt N\,e^{-i\pi\gamma_N}
       e^{\,i\pi[N(z-z^2)-z]}
       \left(1+O_N((1+H)e^{-2\pi H})\right),
 \quad z=x+iH.
 \tag{6}
\]
In particular,
\[
 |\Pi_N(x+iH)|\sim
 \sqrt N\,\exp\{\pi[N(2x-1)+1]H\}.
 \tag{7}
\]
The \(+1\) inside the bracket is retained.

## 2. The original cardinal normalization at both ends

Keep \(y=x_0=\xi+i\eta\), \(Y=e^{2\pi iy}\), with the original
\(0<\xi<1\), \(\eta>0\), and \(0<1-\xi-1/N<1\).
The [global factorial cardinal chart](research_mixed_fourier_global_factorial_cardinal.md)
defines the holomorphic reciprocal continuation \(E_N\) and
\[
 \widehat f_N(q;y)=
 \frac{e^{-\pi i(N-1)y}}N e^{2\pi iNyq}
                    \Pi_N(1-y-1/N)E_N(q-y).
 \tag{8}
\]
On the intersection of \(\Re(q-y)<1\) with either nonreal
half-plane for \(q-y\), the continuation \(E_N\) agrees with
\(1/\Pi_N\), by the original recurrence and the identity theorem.
The zeros of \(E_N\) on the real line are not
removed. Formula (8) agrees with every original physical \(f_l\)
at \(q=l/N\).

Define the two nonzero, fixed-level constants
\[
 \begin{split}
 D_N^- (y)&=
  \frac{\Pi_N(1-y-1/N)}{N^{3/2}}
       e^{-\pi i(N-1)y-i\pi\gamma_N},\\
 D_N^+ (y)&=
  \frac{\Pi_N(1-y-1/N)}{N^{3/2}}
       e^{i\pi(\gamma_N+Ny^2)}.
 \end{split}
 \tag{9}
\]
Equations (4) and (6), with \(z=q-y\), give
\[
 \begin{split}
 \widehat f_N(u-iH;y)
   &=D_N^-(y)e^{2\pi iNy(u-iH)}
           \left(1+O_{N,y}((1+H)e^{-2\pi H})\right),\\
 \widehat f_N(u+iH;y)
   &=D_N^+(y)e^{i\pi[N(u+iH)^2-(N-1)(u+iH)]}
           \left(1+O_{N,y}((1+H)e^{-2\pi H})\right).
 \end{split}
 \tag{10}
\]
Both are uniform on every fixed compact real interval
\(u\in(-\infty,1+\xi)\).
For the second formula the exponent identity is
\[
 \begin{split}
 &-\pi i(N-1)y+2\pi iNyq
       -i\pi[N((q-y)-(q-y)^2)-(q-y)]\\
 &\hspace{25mm}=i\pi[Nq^2-(N-1)q+Ny^2].
 \end{split}
 \tag{11}
\]
This checks all \(N-1\) phases before taking a modulus. In
particular the upper-height cardinal modulus satisfies
\[
 |\widehat f_N(u+iH;y)|
 \sim |D_N^+(y)|e^{\,\pi[N(1-2u)-1]H},
 \quad
 |D_N^+(y)|=
 \frac{|\Pi_N(1-y-1/N)|}{N^{3/2}}e^{-2\pi N\xi\eta}.
 \tag{12}
\]
The exponential slope in (12) contains \(-1\), even at odd \(N\).

## 3. Both complete horizontal aliases vanish

Use the unchanged low-index polynomial and its source:
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(Z)=(rZ;r)_j,\quad
 M_N=\lceil N/2\rceil-1,\\
 A_{j,N}=X^{-j}p_j(X)/P_j^3,\qquad
 C_N^<(X,Z)=\sum_{j=0}^{M_N}A_{j,N}p_j(Z),\\
 \widehat S_N(q)=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y),
 \qquad
 \alpha_N=-1/(2N),\quad \beta_N=\alpha_N+1.
 \end{gathered}
 \tag{13}
\]
No coefficient \(A_{j,N}\) is divided out; it may vanish.
All denominators \(P_j\) are nonzero.

For each fixed \(j\), the exact finite product gives uniformly in
bounded \(u\)
\[
 \begin{split}
 p_j(e^{-2\pi i(u-iH)})&=1+O_N(e^{-2\pi H}),\\
 p_j(e^{-2\pi i(u+iH)})
   &=(-1)^jr^{j(j+1)/2}e^{-2\pi ij(u+iH)}
                     (1+O_N(e^{-2\pi H})).
 \end{split}
 \tag{14}
\]
For \(j=0\) these identities are exact with zero error.
Combining the lower formula in (10) with the exact lower-alias
denominator yields
\[
 \sup_{\alpha_N\le u\le\beta_N}
 \left|
 \widehat S_N(u-iH)
 \frac{e^{-2\pi iN(u-iH)}}{1-e^{-2\pi iN(u-iH)}}
 \right|
 \le C_{N,X,y}e^{-2\pi N(1-\xi)H}
 \tag{15}
\]
for all sufficiently large \(H\). The exponent is strictly negative.

For the upper alias, the \(j\)-th summand has absolute value at most
\[
 C_{N,X,y}
 \exp\{-\pi H[2Nu+N+1-2j]\}.
 \tag{16}
\]
Indeed (12) supplies \(N(1-2u)-1\), the polynomial supplies \(2j\),
and the alias supplies \(-2N\). Since \(u\ge-1/(2N)\),
\[
 2Nu+N+1-2j\ge N-2M_N
 =:\delta_N=
 \begin{cases}2,&N\text{ even},\\1,&N\text{ odd}.\end{cases}
 \tag{17}
\]
Summing the finite number of terms therefore gives
\[
 \sup_{\alpha_N\le u\le\beta_N}
 \left|
 \widehat S_N(u+iH)
 \frac{e^{2\pi iN(u+iH)}}{1-e^{2\pi iN(u+iH)}}
 \right|
 \le C_{N,X,y}e^{-\pi\delta_N H}.
 \tag{18}
\]
It follows that the entire lower and upper horizontal integrals,
including their coefficient \(N\), tend to zero at fixed \(N\).
No exchange of the limits \(H\to\infty\) and \(N\to\infty\) is used.

## 4. The exact remaining boundary current

Fix the original critical height \(h_0<0\) and put
\[
 w_{N,h_0}(v)=\frac1{1+e^{2\pi Nv}}
                         -\boldsymbol1_{\{v<h_0\}}.
 \tag{19}
\]
The exact finite-height identity in the global cardinal note,
together with (15) and (18), implies
\[
 \boxed{
 \begin{split}
 V_N^<={}&N\int_{\alpha_N}^{\beta_N}\widehat S_N(u+ih_0)\,du\\
 &+iN\int_{-\infty}^{\infty}w_{N,h_0}(v)
       [\widehat S_N(\beta_N+iv)-\widehat S_N(\alpha_N+iv)]\,dv .
 \end{split}}
 \tag{20}
\]
The vertical integral is absolutely convergent at this fixed level.
For sufficiently large positive \(v\), its absolute integrand is
bounded by \(C_{N,X,y}e^{-\pi\delta_N v}\), using the same argument
as (18) at the two endpoints. For large negative \(v\),
\[
 |w_{N,h_0}(v)|\le e^{2\pi Nv},\qquad
 |\widehat S_N(\alpha_N+iv)|+
 |\widehat S_N(\beta_N+iv)|
       \le C_{N,X,y}e^{-2\pi N\xi v}.
 \tag{21}
\]
Their product is integrable, since \(1-\xi>0\). On every bounded
vertical interval the continued source is holomorphic and bounded;
the single indicator jump in (19) causes no problem.
These bounds justify the passage to infinite endpoints in the exact
finite-height identity.

The right-minus-left difference in (20) is deliberately undivided.
The exact monodromy is
\[
 (1+Y^Ne^{2\pi Nv})\widehat S_N(\beta_N+iv)
                    =Y^N\widehat S_N(\alpha_N+iv).
 \tag{22}
\]
If its displayed factor vanishes, the original functions are still
regular. A quotient version requires a removable continuation; it
is neither needed nor used in (20).

The residue sum is exactly the original low source because the
added physical rows with \(j+l\ge N\) vanish through \(p_j(r^l)\).
The cardinal \(1/N\), residue \(N\), original retained coefficients,
and both parity cuts are unchanged. Off-grid wrap rows are present
in both integrals in (20).

This removes two complete contour groups, but it does not bound
the two remaining ones at the calibrated action. In particular,
\(h_0<v<0\) has no small Fourier factor in (19), and all constants
used to send the contour to infinity may depend on \(N\).
Neither absolute convergence nor the exact monodromy yields a
uniform volume gap or a whole-source noncancellation theorem.
No numerical evaluation or certificate replay is used.
