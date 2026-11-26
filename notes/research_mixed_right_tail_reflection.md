# Reflection bounds for the complete right real-row tail

Research deduction, 5 November 2026. Every sufficiently late row is
bounded by the literal last-row rate, at arbitrary fixed heights. If
the first height is nonnegative and the second nonpositive, the entire
right half of the row interval is bounded by its half-row. The proof
uses complete product integrals and retains both wrapped rows and the
original first-argument chirp. The other height-sign classes remain
open; no universal endpoint-only tail claim is made.

## 1. The exact reflected rate

Put \(P=[11/50,9/20]\), \(a=x+ih_a\), \(b=z+ih_b\),
with \(x,z\in P\). The heights in the present row inequalities
may be arbitrary finite real numbers. Define
\[
 \begin{split}
 G_H(t)&=\Re g(t-iH),\qquad H\ge0,\\
 f_H(t)&=G_H'(t)=\log|1-e^{-2\pi H-2\pi it}|,\\
 E_\epsilon(u)&=I_{h_a}(u,x)+I_{h_b}(u,z)
             -(2+\epsilon)J(u)-2\pi h_a u,
                       \qquad \epsilon\in\{0,1\},\\
 I_h(u,x)&=\int_0^u\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt.
 \end{split}
 \tag{1}
\]
The primitive \(G_H\) is odd and one-periodic. Also
\[
 J(t)\le G_H(t)\le0\quad(0\le t\le1/2),\qquad
 f_H(t)=f_H(-t),
 \tag{2}
\]
and \(f_H\) is increasing with distance from the nearest integer
on \([0,1/2]\). These facts follow from the radial dilogarithm
identity and the elementary modulus of \(1-re^{-2\pi it}\),
\(0<r\le1\). At \(H=0\), all integrals use their continuous
limits through the integrable logarithmic zeros.

The radial reciprocal identity, with the chirp in (1) retained, gives
\[
 \begin{split}
 E_\epsilon(u)
 ={}&G_{|h_a|}(x+u)-G_{|h_a|}(x)
       +G_{|h_b|}(z+u)-G_{|h_b|}(z)\\
    &-(2+\epsilon)J(u)+\lambda u,\qquad
 \lambda=2\pi\{(-h_a)_++(h_b)_+\}\ge0.
 \end{split}
 \tag{3}
\]
Thus \(E_\epsilon(1)=\lambda\). With \(v=1-u\), the
exact difference from the last row is
\[
 \begin{split}
 \Phi_\epsilon(v)&:=E_\epsilon(1-v)-E_\epsilon(1)\\
 &=G_{|h_a|}(x-v)-G_{|h_a|}(x)
   +G_{|h_b|}(z-v)-G_{|h_b|}(z)
   +(2+\epsilon)J(v)-\lambda v.
 \end{split}
 \tag{4}
\]
The allocated real-row rate in the
[asymmetric-contour theorem](research_mixed_horizontal_asymmetric_contour.md)
adds \(-\eta\Re g(a)/2-\epsilon\Re g(b)/2\) to (1).
Those are constants in \(u\). Every row-difference statement
below therefore holds with the original allocated halfweights as well.
No Fourier branch is changed in making such a comparison.

## 2. All rows past the real targets are bounded by the last row

**Lemma 1.** If \(0\le v\le\min(x,z)\), then
\[
 \Phi_\epsilon(v)\le\epsilon J(v)-\lambda v\le0.
 \tag{5}
\]
Consequently every row \(u\ge1-\min(x,z)\), and in
particular every \(u\ge39/50\), is bounded by the last row.

*Proof.* For fixed \(H\), consider
\(A_H(x,v)=\int_{x-v}^{x}f_H(t)\,dt\). When
\(v\le x\le1/2\), both endpoints lie in the interval of
monotonicity in (2). Hence
\[
 A_H(x,v)\ge A_H(v,v)=G_H(v)\ge J(v).
\]
Since \(G_H(x-v)-G_H(x)=-A_H(x,v)\), use this inequality
twice in (4). Here \(v\le\min(x,z)<1/2\), so
\(J(v)\le0\). This proves (5), including endpoints and
zero-height limits. \(\square\)

## 3. The largest increment above the half-row is at the small-angle corner

**Lemma 2.** For fixed heights and \(1/2\le u\le39/50\),
\[
 E_\epsilon(u;x,z)-E_\epsilon(1/2;x,z)
 \le E_\epsilon(u;11/50,11/50)
                  -E_\epsilon(1/2;11/50,11/50).
 \tag{6}
\]
The heights on the two sides are identical; no new reference is
substituted into this statement about row increments.

*Proof.* The angle-dependent part of either individual increment is
\[
 G_H(x+u)-G_H(x+1/2)
       =\int_{x-1/2}^{x+u-1}f_H(t)\,dt.
 \tag{7}
\]
This is an arc of length \(d=u-1/2\le7/25\), centered at
\(x-c\), where \(c=(3/2-u)/2\in[9/25,1/2]\).
On the present range its endpoints stay in \((-1/2,1/2)\).
Because \(f_H\) is even and increases with absolute argument
there, its integral over an arc of fixed length increases with the
absolute value of the center. This also follows by differentiating
that integral: its derivative is the difference of its two endpoint
values. Among \(x\in[11/50,9/20]\), the center farthest
from zero is always \(x=11/50\), since \(c\ge9/25\)
and \(2c>11/50+9/20\). Thus each integral (7) is maximized
at that endpoint. The own-factorial and \(\lambda\) terms do
not depend on the outer angles. Apply the same argument to \(z\).
\(\square\)

## 4. A complete endpoint-only bound for one height-sign region

**Theorem 1.** If \(h_a\ge0\) and \(h_b\le0\), then
for both own types and every \(x,z\in P\),
\[
          \max_{1/2\le u\le1}E_\epsilon(u;x,z)
                            =E_\epsilon(1/2;x,z).
 \tag{8}
\]
The heights need not be small. This is an upper bound for the entire
real-row tail, not a claim of noncancellation in the finite kernel.

*Proof.* The sign condition is exactly \(\lambda=0\).
First set \(x=z=\ell_0=11/50\). For
\(\ell_0\le v\le1/2\), oddness in (4) gives
\[
 \Phi_\epsilon'(v)
  =(2+\epsilon)\log(2\sin\pi v)
       -f_{|h_a|}(v-\ell_0)-f_{|h_b|}(v-\ell_0)>0.
 \tag{9}
\]
Indeed, for \(0\le r\le1\), convexity of a modulus along
the radial segment gives
\[
 |1-re^{-2\pi it}|\le\max\{1,2\sin\pi t\}
                <2\sin\pi v,
 \quad 0\le t=v-\ell_0<v\le1/2.
 \tag{10}
\]
Here \(2\sin\pi v>1\) because \(v\ge\ell_0>1/6\).
Thus each of the last two logarithms in (9) is smaller than the
first base logarithm. Also that logarithm is positive. Integrating
(9) gives the half-row comparison at the small-angle corner for
\(1/2\le u\le39/50\); Lemma 2 transfers it to every
\((x,z)\in P^2\).

The remaining rows are bounded by the last row by Lemma 1. At
\(\lambda=0\), however,
\[
 \begin{split}
 E_\epsilon(1/2)-E_\epsilon(1)
 ={}&-G_{|h_a|}(1/2-x)-G_{|h_a|}(x)\\
    &-G_{|h_b|}(1/2-z)-G_{|h_b|}(z)>0
 \end{split}
 \tag{11}
\]
for finite heights, by (2) and the strict radial sign in
\(0<t<1/2\). Thus those rows are also bounded by the half-row.
Continuity handles any integrable row zeros. \(\square\)

For the actual unselected horizontal family in the
[half-index contour theorem](research_mixed_half_index_contour.md),
the height sign condition therefore reduces its full real-tail term
to the two real cuts:
\[
 T_*(a,b)=\max\{\mathcal R_\epsilon(3/20;a,b),
                         \mathcal R_\epsilon(1/2;a,b)\}.
 \tag{12}
\]
Combining that theorem with (12) gives its complete finite upper bound
using only the two real-cut comparisons. Their calibrated signs still
need proof; this note does not infer them from (8). The original
actual-height/Fourier and derivative hypotheses of the finite-source
theorem are retained.

## 5. The remaining height signs and the own-type comparison

At general heights \(\lambda>0\), Lemmas 1--2 remain true,
but the derivative in (9) has the additional term \(-\lambda\).
It is not legitimate to erase that term or vary it independently of
the radii \(e^{-2\pi|h_a|},e^{-2\pi|h_b|}\). The unresolved
rows are in the compact interval \([1/2,39/50]\), with the
literal radius/drift correlation (3).

There is one exact simplification for this remaining problem. With
fixed targets and the row-independent halfweight constants canceled,
\[
 \mathcal R_1(u)-\mathcal R_1(t)
 =\mathcal R_0(u)-\mathcal R_0(t)-J(u),
       \qquad t\in\{1/2,1\}.
 \tag{13}
\]
Since \(J(u)\ge0\) on \([1/2,1]\), any endpoint-only
bound for the own-type-three row increments implies the corresponding
own-type-four increment bound at the same targets and heights. This
does not compare the two absolute allocated rates after changing a
type; their different constant halfweights have canceled only in
the displayed differences. No result for all \(\lambda>0\)
is asserted.
