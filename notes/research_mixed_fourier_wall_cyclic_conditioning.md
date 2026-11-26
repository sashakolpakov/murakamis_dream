# Conditioning forced by the actual Wall solution

Research deduction, 7 November 2026. The exact cyclic model has a
positive invariant inner product, but every such inner product is
exponentially distorted relative to the literal Wall coordinates.
This follows from a proved component of the actual finite source,
not from a hypothetical nonnormal matrix. Some exact spectral
projectors likewise have exponentially large specified matrix
entries.

More generally, no subexponentially equivalent positive norm can
make all powers through one period subexponentially bounded.
These conclusions obstruct the direct uniformly equivalent
Plancherel or almost-invariance route. They do not obstruct a norm
whose weights include the original source action and whose
incoming and closing functionals are estimated with those weights.
No new function value or numerical quantity is evaluated.

## 1. The exact operator and an available positive metric

Fix the original \(Y=e^{2\pi ix_0}\), and write
\[
 \rho=|Y|<5/8,\qquad r=e^{-2\pi i/N},\qquad N\ge2.
 \tag{1}
\]
Use \(J=J_N(Y)\), \(T\), and \(C\) from the
[full-period connection theorem](research_mixed_fourier_wall_full_period_connection.md).
Thus
\[
 \begin{gathered}
 A_n=r^n(1-Yr^{n+1}),\qquad C_n=Yr^n(1-r^n),\\
 (Jv)_n=r\{A_n(v_n-v_{n+1})+C_n(v_n-v_{n-1})\},\\
 v_N=0,\qquad C_0=0,\qquad
 JT=TC,\qquad J^N=(1-Y^N)I .
 \end{gathered}
 \tag{2}
\]
Here \(T_{nl}=[u^l]W_{n,N}(u;Y)\). It is invertible, with
the literal polynomial coefficient normalization.
The matrix \(C\) shifts coordinates to the left, with final
entry \((Cv)_{N-1}=(1-Y^N)v_0\).

Choose any \(\mu_N\) with \(\mu_N^N=1-Y^N\), and put
\[
 R_N=|\mu_N|,\qquad
 D_N=\operatorname{diag}(1,\mu_N,\ldots,\mu_N^{N-1}).
 \tag{3}
\]
If \(U\) is the ordinary cyclic shift with final entry \(v_0\),
then \(D_N^{-1}CD_N=\mu_N U\). Hence
\[
 S_N=TD_N,\qquad
 H_N^{\,0}=(S_N^{-1})^*S_N^{-1}>0,\qquad
                 J^*H_N^{\,0}J=R_N^2H_N^{\,0}.
 \tag{4}
\]
This supplies an exact positive inner product in which
\(J/R_N\) is unitary. It uses neither real-base orthogonality
nor positivity of the finite quantum source.

The diagonal normalization in (3) is harmless by itself:
\[
 \frac{39}{64}<1-\rho^N\le |1-Y^N|\le1+\rho^N<\frac{89}{64}.
 \tag{5}
\]
Every diagonal modulus of \(D_N\) consequently lies between
\(39/64\) and \(89/64\), so
\(\operatorname{cond}_2(D_N)<89/39\).
The coefficient change \(T\) cannot have comparable conditioning,
as the next sections show.

## 2. A forced exponential component of the actual solution

Let
\[
 {\bf W}_N=(W_{0,N}(Y;Y),\ldots,W_{N-1,N}(Y;Y))^T,\qquad
 m_N=\lfloor N/2\rfloor .
 \tag{6}
\]
The completed [half-degree theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md)
proves
\[
 W_{m_N,N}(Y;Y)
   ={\cal A}(m_N/N,Y)\exp\{NI(m_N/N,Y)\}(1+O(N^{-1})).
 \tag{7}
\]
Its coefficient is nonzero. Its exterior degree root satisfies
\(|R(t,0,Y)|>1\) on the whole interval \(0\le t\le1/2\).
Therefore the fixed original action
\[
       \gamma=\Re I(1/2,Y)
              =\int_0^{1/2}\log|R(t,0,Y)|\,dt>0
 \tag{8}
\]
is strictly positive. No value of \(\gamma\) is needed here.
The uniform nonzero amplitude and bounded action derivative in
(7) imply that there are \(c>0\) and \(N_0\) such that
\[
                   |W_{m_N,N}(Y;Y)|\ge c e^{\gamma N}
                                     \qquad(N\ge N_0).
 \tag{9}
\]
The displacement \(m_N/N-1/2=O(N^{-1})\) changes the exponent
by a bounded amount. Thus (9) includes both parities.

The canceled terminal value and the exact endpoint defect are
\[
 {\cal W}_N(Y;Y)=\frac{1-2Y^N}{1-Y^N}\ne0,\qquad
 (J-YI){\bf W}_N=(1-Y){\cal W}_N(Y;Y)e_{N-1}.
 \tag{10}
\]
For \(N\ge2\),
\[
 |{\cal W}_N(Y;Y)|
       \le\frac{1+2\rho^N}{1-\rho^N}<3,\qquad
                 |(1-Y){\cal W}_N(Y;Y)|<6.
 \tag{11}
\]
Hence a bounded, explicitly specified forcing vector has the
exponentially large actual response (9).

There is nevertheless a fixed spectral gap from this forcing
parameter. All eigenvalues of \(J\) have modulus \(R_N\).
Set \(b=(1-\rho^2)^{1/2}\). Since \(b^N+\rho^N\le b^2+\rho^2=1\),
\[
 R_N\ge(1-\rho^N)^{1/N}\ge b
      >\frac{\sqrt{39}}8>\frac34,\qquad
                     R_N-\rho>\frac18 .
 \tag{12}
\]
In particular \(Y\) is never an eigenvalue. The large response is
not a small eigenvalue denominator.

## 3. Invariant metrics and almost-invariant norms

For a positive Hermitian matrix \(H\), let
\(\|v\|_H^2=v^*Hv\), and write
\(\kappa_2(H)=\lambda_{\max}(H)/\lambda_{\min}(H)\).

**Proposition 1.** Every positive \(H\) satisfying
\[
                          J^*HJ=R_N^2H
 \tag{13}
\]
obeys
\[
 \boxed{\displaystyle
 \kappa_2(H)\ge
       \frac{|W_{m_N,N}(Y;Y)|^2}{48^2}
       \ge\frac{c^2}{48^2}e^{2\gamma N}
 \qquad(N\ge N_0).}
 \tag{14}
\]
The same conclusion applies if (13) is initially assumed only
with \(\le\).

*Proof.* Under (13), \(H^{1/2}JH^{-1/2}/R_N\) is unitary.
Equation (12) gives
\(\|(J-YI)^{-1}\|_H<8\). Applying this to (10), and converting
the input and output norms separately, yields
\[
 |W_{m_N,N}|
 \le\|{\bf W}_N\|_2
 \le\frac{\|{\bf W}_N\|_H}{\sqrt{\lambda_{\min}(H)}}
 <48\sqrt{\kappa_2(H)} .
 \tag{15}
\]
This proves (14). If \(J^*HJ\le R_N^2H\), the normalized
conjugate is a contraction, while the modulus of its determinant
is one by (2). All its singular values are at most one and their
product is one. They are therefore all one, reducing to (13).
\(\square\)

There is also an obstruction without exact unitarity.
Define
\[
                    P_N(H)=\max_{0\le d<N}\|J^d\|_H .
 \tag{16}
\]
The exact polynomial recovery in the full-period theorem gives
\[
 {\bf W}_N=\frac{1-Y}{1-Y^N}
                  \sum_{d=0}^{N-1}Y^dJ^{N-1-d}e_{N-1}.
 \tag{17}
\]
Here
\[
 \left|\frac{1-Y}{1-Y^N}\right|<3,\qquad
                    \sum_{d=0}^{N-1}\rho^d<8/3 .
 \tag{18}
\]
Thus, for every positive \(H\),
\[
 \boxed{\displaystyle
       P_N(H)\sqrt{\kappa_2(H)}
                 \ge\frac{|W_{m_N,N}(Y;Y)|}{8}
                 \ge\frac c8 e^{\gamma N}.}
 \tag{19}
\]
The proof is simply the triangle inequality in (17), followed by
the two norm conversions used in (15).

Consequently a family of positive norms with
\(\log\kappa_2(H_N)=o(N)\) cannot also have
\(\log P_N(H_N)=o(N)\). In particular it cannot make
\(\|J\|_{H_N}\le1+o(1)\), since that bound would imply
\(P_N(H_N)\le(1+o(1))^{N-1}=e^{o(N)}\).
This conclusion concerns powers through one actual finite period;
no exchange of a large-power and a large-level limit occurs.

## 4. The actual spectral coefficient is also large

Let \(\lambda_k=\mu_Nr^k\), \(0\le k<N\). The spectral projectors
have the exact finite Fourier formula
\[
                 {\cal P}_k
            =\frac1N\sum_{d=0}^{N-1}\lambda_k^{-d}J^d,
 \qquad
                  (J-YI)^{-1}
            =\sum_{k=0}^{N-1}\frac{{\cal P}_k}{\lambda_k-Y}.
 \tag{20}
\]
The simple spectrum and \(J^N=(1-Y^N)I\) prove these identities
directly, by evaluating the polynomials at each eigenvalue.
Taking the \(m_N\)-th component of (10) and using (11)--(12),
\[
 \boxed{\displaystyle
 \max_{0\le k<N}|({\cal P}_k)_{m_N,N-1}|
       \ge \frac{|W_{m_N,N}(Y;Y)|}{48N}
       \ge \frac{c}{48N}e^{\gamma N}.}
 \tag{21}
\]
Thus exponential size is unavoidable even for this specified
input/output entry, not merely for an unspecified operator norm.
It is consistent with
\(\sum_k{\cal P}_k=I\): these entries may cancel in their sum.
An averaged spectral identity does not remove that cancellation.

Equations (14), (19), and (21) do not show that the original
contracted source is too large. Its component is
\[
 H_{j,N}(y)=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
                P_jW_{N-j-1,N}(Y;Y),
 \tag{22}
\]
followed by the literal incoming coefficients and allocation.
The action in (8) is part of its proved geometric behavior.
A source-adapted norm may intentionally absorb that exponential
action and then estimate both the incoming and closing factors.
What is ruled out is obtaining those estimates merely by passing
to a positive cyclic norm or finite Fourier projectors at a
subexponential cost in the literal Wall coordinates.

No lower bound for the remaining low-index source or for a knot
invariant is inferred. The exact two-sided connection and a
coherent, action-calibrated analysis remain available routes.
