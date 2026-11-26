# The marked figure-eight cusp and the first microscopic curvature

Private calculation, 31 October 2026. This fixes the sign, primitive longitude, and factor of two directly from the actual braid. The last section records the resulting interpretation of the source asymptotic; it uses the separate positive-concentration argument described there.

## 1. The actual braid and its preferred longitude

Use the action-ordered braid
\[
(\sigma_1,\sigma_2^{-1},\sigma_1,\sigma_2^{-1})
\]
and the actual Hurwitz convention of [the longitude calculation](/Users/sasha/volume-conjecture/notes/quantum_longitude_and_regulator_action.md). Let
\[
A=\begin{pmatrix}M&1\\0&M^{-1}\end{pmatrix},\qquad
B=\begin{pmatrix}M&0\\t&M^{-1}\end{pmatrix},\qquad
C=A^{-1}BAB^{-1}A.
\tag{1}
\]
The closure equation is
\[
t^2+(M^2+M^{-2}-3)t+3-M^2-M^{-2}=0.
\tag{2}
\]
Set \(D=A^{-1}BA\), \(E=CAC^{-1}\). The four successive meridian tuples and strand labels are
\[
\begin{array}{c|c|c}
&\text{meridian tuple}&\text{original strand labels}\\ \hline
\text{initial}&(A,B,C)&(0,1,2)\\
\sigma_1&(D,A,C)&(1,0,2)\\
\sigma_2^{-1}&(D,C,E)&(1,2,0)\\
\sigma_1&(D^{-1}CD,D,E)&(2,1,0)\\
\sigma_2^{-1}&(D^{-1}CD,E,EDE^{-1})&(2,0,1).
\end{array}
\tag{3}
\]
Reduction using (2) gives \(D^{-1}CD=A\), \(E=B\), and \(EDE^{-1}=C\). These are matrix identities, not a numerical closure check.

The left-ordered underpass transport accumulated by original strands \(0,1,2\) is respectively
\[
C,\qquad BA^{-1},\qquad D^{-1}.
\]
Following the closed knot from strand \(0\) visits those strands in the order \(0,1,2\). Thus
\[
W=D^{-1}BA^{-1}C.
\tag{4}
\]
The writhe is zero. The actual preferred longitude is therefore
\[
\boxed{\quad
\lambda=W^{-1}=C^{-1}AB^{-1}D
=C^{-1}AB^{-1}A^{-1}BA.
\quad}
\tag{5}
\]
This is precisely the convention \(\lambda=W^{-1}\mu^{-w}\) of the original source, with \(w=0\). Reversing this word would change the cusp sign.

At \(M=1\), (2) becomes \(t^2-t+1=0\), and direct multiplication gives
\[
W=\begin{pmatrix}-1&2-4t\\0&-1\end{pmatrix},
\qquad
\lambda=\begin{pmatrix}-1&4t-2\\0&-1\end{pmatrix}.
\tag{6}
\]
The preferred longitude has central sign \(-1\). Its projective action, or equivalently the action of the centered matrix \(-\lambda\), is translation by \(2-4t\). The meridian \(A\) translates by \(1\).

The [actual Bloch specialization](/Users/sasha/volume-conjecture/notes/figure_eight_bloch_specialization.md) selects
\[
t=\frac{1-\sqrt{-3}}2,\qquad
z_{\mathrm{shape}}=\frac{1+\sqrt{-3}}2.
\tag{7}
\]
The shape in (7) is in the upper half-plane and gives positive fundamental-class volume; the Riley parameter is its conjugate. Hence the actual oriented primitive cusp shape is
\[
\boxed{\quad \tau=2-4t=2\sqrt3\,i.\quad}
\tag{8}
\]
This conclusion retains the longitude sign in (6); using \(-\lambda\) to read a projective translation does not change the actual preferred-longitude lift.

## 2. The same derivative on the marked peripheral curve

For completeness, reduction of (5) using (2) gives the upper-triangular matrix
\[
\lambda=
\begin{pmatrix}
M^4-2M^2-1+M^{-2}+(M^2-M^{-2})t&
\dfrac{(M^2+1)(M^4+2M^2t-3M^2+1)}{M^3}\\
0&
-\dfrac{M^6t-M^6+M^4-M^2t+2M^2-1}{M^4}
\end{pmatrix}.
\tag{9}
\]
Its determinant is one, and
\[
\operatorname{Tr}\lambda
=M^4+M^{-4}-M^2-M^{-2}-2.
\tag{10}
\]
The eigenline of \(A\) with eigenvalue \(M\) is its first coordinate line. Therefore \(L_{\mathrm{intr}}=\lambda_{11}\), with the upper-left entry understood in (9), is exactly the preferred eigenvalue used by the actual source. It satisfies \(L_{\mathrm{intr}}(1)=-1\) and the corresponding quadratic peripheral equation obtained from (10).

Set \(u=\operatorname{Log}M\). Differentiating (9) at \(M=1\) gives
\[
\left.\frac{d\log L_{\mathrm{intr}}}{du}\right|_{u=0}
=2-4t=2\sqrt3\,i.
\tag{11}
\]
There is no contribution from \(t'(0)\), because its coefficient \(M^2-M^{-2}\) vanishes there; (2) also gives \(t'(0)=0\). The centered longitude eigenvalue \(\ell=-L_{\mathrm{intr}}\) has the same logarithmic derivative. In squared-eigenvalue coordinates
\[
U=2\log M,\qquad V=2\log\ell,
\]
the ratio \(dV/dU\) remains \(\tau\), with no additional factor of two.

As a check from the curve alone, writing \(L_{\mathrm{intr}}=-e^v\) in (10) gives
\(-2\cosh v=-2+12u^2+O(u^4)\), so the two slopes are \(\pm2\sqrt3 i\). The matrix word and the positive Bloch orientation select the plus sign in (11); the polynomial alone does not.

## 3. Interpretation of the first microscopic correction

The actual source identity gives positive complete weights
\[
a_{N,n}=\prod_{r=1}^n4\sin^2(\pi r/N),\qquad
K_N=\sum_{n=0}^{N-1}a_{N,n}.
\]
At \(Y=e^{z/N}\) the \(n\)-th summand is multiplied by
\[
P_{N,n}(z)=
\prod_{r=1}^n\left(1+
\frac{\sinh^2(z/(2N))}{\sin^2(\pi r/N)}\right).
\tag{12}
\]
The exact peripheral factor is
\[
H_N(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))}.
\]
The canonical regular profile obeys \(g_N=H_N\rho_N+\pi_N\), where \(g_N=F_N(e^{z/N})/K_N\) and the ordinary-color interpolation term \(\pi_N\) is exponentially small on fixed compact sets.

Here is the coefficient calculation supporting the separate concentration proof. For \(x=n/N\) in a compact interval containing \(5/6\) and lying inside \((1/2,1)\), the reflection \(r\mapsto N-r\) and the exact product for \(H_N\) cancel the endpoint factors in \(P_{N,n}/H_N\). For odd \(N=2m+1\), the quotient is the product over \(r=m+1,\ldots,n\). For even \(N=2m\), it is \(\cosh(z/(2N))\) times the product over \(r=m+1,\ldots,n\). Uniformly on a fixed complex \(z\)-disk this gives
\[
\begin{aligned}
\log\frac{P_{N,n}(z)}{H_N(z)}
&=\frac{z^2}{4N^2}
\sum_{r=\lfloor N/2\rfloor+1}^n\csc^2(\pi r/N)
+O(N^{-2})\\
&=-\frac{z^2\cot(\pi n/N)}{4\pi N}
+O(N^{-2}).
\end{aligned}
\tag{13}
\]
The even midpoint factor has logarithm \(O(N^{-2})\) and does not alter the displayed coefficient. The Riemann-sum error is uniform because this interval stays away from the endpoint \(1\).

The already established positive Laplace concentration puts \(n/N\to5/6\) under the probabilities \(a_{N,n}/K_N\), with exponentially small mass outside every fixed neighborhood. Since \(\cot(5\pi/6)=-\sqrt3\), (13) yields, first on a zero-free enclosing circle for \(H_N\),
\[
N(\rho_N(z)-1)\longrightarrow
\frac{\sqrt3}{4\pi}z^2.
\tag{14}
\]
For the tail needed in this step, (12) is uniformly bounded on every fixed disk for all \(n\), using
\(\sinh^2(z/(2N))=O(N^{-2})\) and
\(\sum_{r=1}^{N-1}\csc^2(\pi r/N)=O(N^2)\).
Thus its exponentially small complete mass remains negligible after multiplication by \(N\). The ordinary-color interpolation term is negligible for the same reason. The functions in (14) are entire; a fixed enclosing circle avoiding the limiting zeros of \(H_N\) and the maximum principle extend the convergence through all those zeros. Cauchy's formula gives convergence of every fixed derivative on smaller disks.

Combining (8) and (14), the coefficient has the exact marked interpretation
\[
\boxed{\quad
N(\rho_N(z)-1)\longrightarrow\frac{\tau}{8\pi i}z^2,
\qquad
N\rho_N''(0)\longrightarrow\frac{\tau}{4\pi i}
=\frac{\sqrt3}{2\pi}.
\quad}
\tag{15}
\]
The finite normalization, the sign of the preferred longitude, and the microscopic coordinate \(M=e^{z/(2N)}\) are all used here. This is a statement proved from the actual positive figure-eight source. It does not infer the analogous correction for a general knot from its peripheral curve.

The marked action identity \(dS_{\mathrm{flat}}=2\log L_{\mathrm{intr}}\,du\) independently predicts the same quadratic coefficient: after recording its complete longitude character, the quadratic term is \(\tau u^2\). Dividing by \(\log Q=2\pi i/N\) and putting \(u=z/(2N)\) gives \(\tau z^2/(8\pi iN)\). This explains the agreement of the two independently obtained coefficients. It does not remove the complete sign character or replace the finite-source proof.

