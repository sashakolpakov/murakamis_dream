# A strict half-input overlap improvement for the complete two-step source

Private source estimate, 9 November 2026. The complete two-step
conditional kernel has a sharper bound than the general Gram
operator estimate. Its actual incoming column and the row norm
of the original crossing concentrate at different real indices.
Retaining this separation gives a fixed written rate improvement,
including both conditional types and every row from the half input
through the last row. No numerical evaluation is used.

The proof improves a complete-source upper bound. It neither
identifies that bound with a critical action nor compares it with
the next geometric reference.

## 1. Exact third-moment reduction

Use the notation of
[the complete two-step Gram theorem](research_mixed_next_two_step_gram_fourier_bound.md):
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(W)=(rW;r)_j,\\
f_j(W)=p_j(W)/P_j,\qquad
\mathsf F_{ja}=f_j(r^a),\qquad
\mathsf D_\beta=\operatorname{diag}(P_j^{-\beta}),\quad\beta=0,1,\\
K=\mathsf F^*\mathsf F
 =\mathsf U\mathsf H\mathsf U^*,\qquad
\mathsf H=\mathsf M^*\mathsf M,\qquad
\mathsf U=\operatorname{diag}((-q)^{-a}).
\end{gathered}                                                       \tag{1}
\]
Here \(\mathsf M\) is the original full crossing matrix,
including its normal directions. The exact positive conjugacy
is the one in
[the original forcing Gram theorem, (6)](research_mixed_next_actual_forcing_gram_bounds.md).
The symbols \(\mathsf D_\beta\) retain their complex phases.

The full two-step polynomial is
\[
\begin{split}
C^{(2)}_{0\beta,N}(r^b,W)
 &=\sum_{a=0}^D C_{0,N}(r^b,r^a)C_{\beta,N}(r^a,W)\\
 &=\mathbf f(r^b)^*(\mathsf F\mathsf F^*)
                         \mathsf D_\beta\mathbf f(W).
\end{split}                                                         \tag{2}
\]
There is no intermediate old-four weight. Apply Cauchy--Schwarz
in this actual feature space, before replacing the first factor
by an operator norm:
\[
\boxed{\quad
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le \sqrt{(K^3)_{bb}}\,
                         \|\mathsf D_\beta\mathbf f(W)\|_2 .
\quad}                                                             \tag{3}
\]
Indeed \(\mathbf f(r^b)=\mathsf F e_b\), and
\[
\|(\mathsf F\mathsf F^*)\mathsf F e_b\|_2^2=(K^3)_{bb}.
\]
The diagonal unitary in (1) then gives the exact identity
\[
\sqrt{(K^3)_{bb}}
 =\sqrt{(\mathsf H^3)_{bb}}
 =\|\mathsf M\mathsf H e_b\|_2
 =\|\mathsf M\mathsf M^*\mathsf M e_b\|_2 .                         \tag{4}
\]
No positivity of \(C_{1,N}\), or of an ordinary Hermite
contraction, is required.

For clarity, the following finite inequality retains the column
in (4). Let \(r_j^{\mathsf M}\) be row \(j\) of \(\mathsf M\),
and put \(v=\mathsf M e_b\). Then
\[
|(\mathsf M\mathsf M^*v)_i|
 \le \|r_i^{\mathsf M}\|_2
          \sum_{j=0}^D\|r_j^{\mathsf M}\|_2\,|v_j|.
\]
Taking the Euclidean norm in \(i\) proves
\[
\boxed{\quad
\sqrt{(K^3)_{bb}}
 \le \|\mathsf M\|_{\rm HS}
        \sum_{j=b}^D\|r_j^{\mathsf M}\|_2\,|\mathsf M_{jb}|.
\quad}                                                             \tag{5}
\]
The lower endpoint \(j=b\) is exact triangular support. Every
entry up to \(j=D\) remains in this inequality. It is a rowwise
triangle and Cauchy estimate, not an assumed almost-invariant
state.

## 2. Uniform row and column profiles

Write
\[
J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
c=-2J(1/6)=-3J(1/3),
\]
\[
E(z,a)=J(z)-J(a)-J(z-a),\qquad
R(z)=J(z)-2J(z/2),\qquad
V(a)=-2J((1-a)/2)-J(a).
                                                                    \tag{6}
\]
The entropy \(E\) is continuous on \(0\le a\le z\le1\).
The original crossing entries are
\[
\mathsf M_{jb}
 =\kappa(-1)^j q^{j(b+1)}
                       \frac{S_j}{S_bS_{j-b}},\qquad b\le j,
\quad |\kappa|=1 .                                                 \tag{7}
\]
These are the full original coefficients in
[the one-crossing theorem, (1)--(5)](research_one_crossing_gaussian_window.md).
Its endpoint-uniform sine-factorial estimate gives
\[
|\mathsf M_{jb}|\le CN^A e^{NE(j/N,b/N)}.                           \tag{8}
\]
All factorial indices in (7) lie between zero and \(D\);
no vanishing denominator occurs.

For fixed \(z\), \(E(z,a)\) has its maximum at \(a=z/2\),
with value \(R(z)\). This follows either from its strict
concavity or directly from
\[
E_a(z,a)=\log\frac{\sin\pi(z-a)}{\sin\pi a}.
\]
Continuity covers the endpoints \(z=0,1\). Summing the
at most \(N\) squares in a row therefore gives
\[
\|r_j^{\mathsf M}\|_2\le CN^A e^{NR(j/N)}.                         \tag{9}
\]
Moreover
\[
R'(z)=\log(2\cos(\pi z/2)),\qquad
R(2/3)=c,
\]
so \(R\) has its unique maximum at \(2/3\). Equations (8)--(9),
or the original whole-matrix norm theorem, imply
\[
\|\mathsf M\|_{\rm HS}\le CN^A e^{Nc}.                            \tag{10}
\]
Thus (5) yields, uniformly for every physical \(b\),
\[
\sqrt{(K^3)_{bb}}
 \le CN^A\exp N\left\{
 c+\max_{b/N\le z\le1}[R(z)+E(z,b/N)]\right\}.
                                                                    \tag{11}
\]
Using the closed interval in this maximum only enlarges the
literal finite sum. Equations (8)--(11) are uniform even when
\(b/N\) or \(j/N\) tends to one.

## 3. A quantitative separation at and above the half input

For \(1/2\le a<1\), the maximum of \(E(z,a)\) as a function
of \(z\in[a,1]\) occurs at
\[
                          z_a=(1+a)/2
\]
and equals \(V(a)\), as in the complete Gram theorem.
Its second derivative satisfies
\[
E_{zz}(z,a)
 =-\frac{\pi\sin\pi a}{\sin\pi z\,\sin\pi(z-a)}
 \le-2\pi\tan(\pi a/2)\le-2\pi .                                  \tag{12}
\]
The first inequality uses
\[
\sin\pi z\,\sin\pi(z-a)
 =\frac{\cos\pi a-\cos\pi(2z-a)}2
 \le\cos^2(\pi a/2).
\]
Both denominator factors are positive in the open interval.
The limiting inequalities for \(E\) itself extend continuously
to \(z=a,1\).

Similarly, for \(1/2\le z<1\),
\[
                R''(z)=-\frac{\pi}{2}\tan(\pi z/2)
                                      \le-\frac{\pi}{2}.           \tag{13}
\]
The segment between \(z\) and \(2/3\) stays in \([1/2,1]\).
Integrating (12)--(13) about their respective maxima gives
\[
R(z)\le c-\frac{\pi}{4}(z-2/3)^2,\qquad
E(z,a)\le V(a)-\pi(z-z_a)^2.                                      \tag{14}
\]
Completing the square, or minimizing a positive quadratic, gives
\[
\frac14(z-2/3)^2+(z-z_a)^2
 \ge\frac15(z_a-2/3)^2
 =\frac{(3a-1)^2}{180}.
\]
Consequently
\[
\boxed{\quad
\max_{a\le z\le1}[R(z)+E(z,a)]
 \le c+V(a)-L(a),\qquad
L(a):=\frac{\pi(3a-1)^2}{180},
\quad 1/2\le a\le1.
\quad}                                                             \tag{15}
\]
The case \(a=1\) follows by continuity on the closed entropy
triangle; it is not obtained by substituting into the derivative
with vanishing sine factors. The loss \(L\) increases on
\([1/2,1]\), and
\[
                              L(1/2)=\frac{\pi}{720}.              \tag{16}
\]

This is the source of the improvement: the row peak \(2/3\)
cannot coincide with the incoming-column peak \((1+a)/2\)
when \(a\ge1/2\).

## 4. The complete kernel and its propagated Fourier contribution

Retain the output profile of the complete Gram theorem:
\[
B_\beta(W)=\max_{0\le s\le1}
 \left\{\int_0^s\log|1-We^{-2\pi iu}|\,du
                                      -(1+\beta)J(s)\right\}.
                                                                    \tag{17}
\]
For every fixed compact \(\mathcal K\subset\mathbb C\) and every
\(\epsilon>0\), that theorem proves, through all numerator zeros,
\[
\|\mathsf D_\beta\mathbf f(W)\|_2
 \le C_\epsilon N^{A_\epsilon}e^{N[B_\beta(W)+\epsilon]},
 \qquad W\in\mathcal K,\quad\beta=0,1 .                            \tag{18}
\]
In particular its \(j=D\) feature and the revived top output
coefficient have not been discarded.

**Theorem.** Put \(M=\lceil N/2\rceil\), \(U=D-M\).
For both parities, every \(M\le b\le D\), both \(\beta=0,1\),
and every \(W\in\mathcal K\),
\[
\boxed{\quad
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le C_\epsilon N^{A_\epsilon}
 \exp N\{2c+V(b/N)+B_\beta(W)-L(b/N)+\epsilon\}.
\quad}                                                             \tag{19}
\]
This follows directly from (3), (11), (15), and (18).
All constants are independent of the physical indices.

The exact complete propagated right contribution still has
the original Fourier representation
\[
(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)
 =\frac1{\kappa^2N}\sum_{k=0}^U
                      f_{k,N}^{(2,\beta)}(W)\mathcal O_{N,k}(w),
\]
\[
f_{k,N}^{(2,\beta)}(W)
 =(-1)^{M+k}\sum_{d=k}^Uq^{M+d}\beta_{d,k,N}
                           C^{(2)}_{0\beta,N}(r^{M+d},W).
                                                                    \tag{20}
\]
The full positive transition, all normals, the odd simple node,
and both Fourier sectors are the ones bound in the preceding
Gram theorem. Its endpoint maximization says
\[
V(1/2+x)+\mathcal H(x,t)+\Gamma(1/2-t)
 \le V(1/2)+\Gamma(1/2),\qquad0\le t\le x\le1/2,
                                                                    \tag{21}
\]
with equality only at \(x=t=0\). Since \(L(1/2+x)\ge L(1/2)\),
the sharpened continuous envelope has the exact maximum
\[
\begin{split}
\max_{0\le t\le x\le1/2}
 \{2c+B_\beta(W)+V(1/2+x)-L(1/2+x)
                       +\mathcal H(x,t)+\Gamma(1/2-t)\}\\
 =2c+B_\beta(W)+V(1/2)+\Gamma(1/2)-\pi/720 .
\end{split}                                                        \tag{22}
\]
It is attained only at \(x=t=0\).

At even levels \((M+d)/N=1/2+d/N\). At odd levels it is larger
by \(1/(2N)\). On \([1/2,1]\), \(V\) decreases and \(L\)
increases, so the odd shift only improves the corresponding
upper bound. Inserting (19) into (20), applying (21)--(22)
and the full observation bound, and summing the at most \(N^2\)
terms proves
\[
\boxed{\quad
\sup_{w\in[-2,2]}
|(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)|
 \le C_\epsilon N^{A_\epsilon}
 e^{N[2c+B_\beta(W)+V(1/2)+\Gamma(1/2)-\pi/720+\epsilon]} .
\quad}                                                             \tag{23}
\]
The same estimate bounds the sum of the absolute complete mode
contributions. The exact scalar \(\kappa^{-2}/N\) in (20)
has modulus \(1/N\); it has not been renormalized. The crossing
scalar in (7) also has unit modulus.

Equation (23) is a strict improvement for the actual all-row
two-step source over the general operator bound. It is still
an upper ceiling. Neither (22) nor its endpoint location asserts
that the signed polynomial attains that ceiling at any prescribed
output. No comparison with the next geometric action, estimate
for the propagated left remainder, or whole closing theorem
follows from this calculation.

## Frozen source versions

- Complete two-step Gram source, zero-safe output profile, exact
  Fourier transition and endpoint maximization:
  be5dc00fde7c062f7b6ad0e7b8859b2e9dd5d564f16bce0aea75de9dba12cb6e.
- Original physical Gram conjugacy:
  77354837ae73521349d7cc3834797c4c81dcae11f69ef1aa705223dec85ad5e8.
- Full one-crossing coefficients and uniform entropy bounds:
  d5d8611da7158539ee73af5413ab2f59da50afe5d3d43dcf2631f4c28f373683.

