# Exact simultaneous contour deformation for a terminal filling

Research note, 2 November 2026. This note supplies an exact
two-variable contour identity for the finite terminal source. It
justifies moving the wire and filling variables together. No estimate
on a deformed face, no dominance assertion, and no asymptotic volume
identity is asserted here.

The proposed contour is described in
[the contour observations](research_terminal_joint_contour_observations.md).
The canonical factorial is defined and proved in
[the factorial section of the Conway asymptotics paper](../papers/conway-asymptotics/factorial.tex).

## 1. An exact holomorphic interpolation of the two-variable summand

Fix \(N\geq3\), put \(d=N-1\), and use the normalized factorial
\(G_N\) satisfying

\[
G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),
\qquad
G_N(k)=S_k\quad(0\leq k<N).
\]

It is holomorphic and nonzero for \(-1<\Re z<N\). Its reciprocal has
a larger holomorphic domain:

**Lemma.** The function \(1/G_N(z)\) extends holomorphically to
\(\Re z<N\).

**Proof.** For any point in that half-plane, choose an integer
\(m\geq0\) so that a neighborhood of \(z+m\) lies in
\(-1<\Re(z+m)<N\). The recurrence gives

\[
\frac1{G_N(z)}
=\frac{\displaystyle\prod_{a=1}^{m}
                   2\sin\frac{\pi(z+a)}N}
       {G_N(z+m)}.
\]

The right side is holomorphic there. The recurrence makes these
definitions agree on overlaps. Zeros of the sine factors are zeros
of the reciprocal, not poles. \(\square\)

Define

\[
\mathcal E_N(x,t)=
\frac{
 G_N(d/2+Nt/(2\pi))G_N(d/2-Nt/(2\pi))}
 {G_N(d/2-Nx+Nt/(2\pi))
  G_N(d/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
                                                        \tag{1}
\]

Reciprocals in this formula use the preceding continuation. For every
integer \(0\leq k<N\), the factorial recurrence gives exactly

\[
\mathcal E_N(k/N,t)
=\frac1{S_k^2}\prod_{a=0}^{k-1}
 \left(2\cos\frac{(2a+1)\pi}{N}+2\cos t\right)
=e_k(-2\cos t).                                         \tag{2}
\]

In particular, (1) is an interpolation of the original polynomial
summands, including their derivatives with respect to \(t\).

For a fixed cutoff \(T<\pi\), (1) is holomorphic on a neighborhood of
the product of strips

\[
-\frac1{2N}\leq\Re x\leq1-\frac1{2N},
\qquad |\Re t|\leq T.
                                                        \tag{3}
\]

Imaginary parts may range over any fixed bounded set. To check this,
the numerator arguments lie strictly between \(-1\) and \(N\) in
real part. Every denominator argument has real part less than \(N\);
the largest of the two shifted denominator arguments on (3) is
\(N/2+NT/(2\pi)<N\). Also \(\Re(Nx)\leq N-1/2<N\).
Shrinking or enlarging the real boundaries slightly preserves these
strict inequalities. The same statement holds with a small complex
parent angle \(u\) in place of \(t\).

For an integer crossing power \(n\), set

\[
f_N(x,t;u)=
\sin t\,\mathcal E_N(x,t)\mathcal E_N(x,u)
\exp\left(\frac{inN}{4\pi}t^2\right).
                                                        \tag{4}
\]

This is the exact interpolated summand of the original wire sum and
leaf trace. It is holomorphic on the domains just described and is
odd in \(t\). Thus crossing the boundary
\(\Re(1/2-x-t/(2\pi))=0\) of the usual factorial asymptotic strip
does not, by itself, create a pole of the exact integrand.

### The exact negative-factorial formula

The small reflection identity for \(G_N\), followed by analytic
continuation, gives, for \(0<\Re w<N\),

\[
\frac1{G_N(-w)}
=G_N(w)\frac{\sin\pi w}{N\sin(\pi w/N)}
=\frac2N\sin(\pi w)G_N(w-1).                           \tag{5}
\]

The final expression has a removable singularity at \(w=0\) when
kept as a product. The sine contains two exponentials,

\[
\frac2N\sin(\pi w)
=\frac{e^{i\pi w}-e^{-i\pi w}}{iN}.
\]

Both belong to the exact continuation. Keeping only one of them is
not an identity. Moreover, splitting them into separate terms across
\(w=0\) introduces poles of \(G_N(w-1)\) that cancel only in their
sum. A contour argument may use (5) without splitting it, or split
on regions separated from those removable singularities.

## 2. The finite two-variable residue formula

Let \(I=[a,b]\) have endpoints halfway between successive wire nodes
\(k/N\). It can enclose all \(0\leq k<N\), using
\(a=-1/(2N)\) and \(b=1-1/(2N)\), or a specified consecutive subset.

Write

\[
\tau_j(\sigma)=\frac{2\pi}{N}
       \left(\frac d2+\sigma-j\right),
\qquad
\delta_\sigma=\frac{2\pi\sigma}{N}.
\]

Choose \(T_N\to T<\pi\) halfway between successive real trace nodes,
and let

\[
J_N=\{j:|\tau_j(0)|<T_N\},\qquad
J_\sigma=[-T_N,T_N]+\delta_\sigma.
\]

The set \(J_N\) is invariant under \(j\mapsto d-j\).
Let \(\Gamma_x\) and \(\Gamma_t(\sigma)\) be the positively oriented
rectangles surrounding \(I\) and \(J_\sigma\), with heights
\(\pm h_x\) and \(\pm h_t\), respectively. The heights are positive.
All rectangles are chosen within a domain where (4) is holomorphic.

Use the two residue-one kernels

\[
\mathscr K_x(x)=\pi N\cot(\pi Nx),
\qquad
\mathscr K_{t,\sigma}(t)=\frac N2
 \cot\left(\frac{Nt}{2}-\pi\left(\frac d2+\sigma\right)\right).
\]

Then

\[
\begin{aligned}
S_N(\sigma,u)
&:=\sum_{\substack{k/N\in I\\j\in J_N}}
             f_N(k/N,\tau_j(\sigma);u)\\
&=\frac1{(2\pi i)^2}
 \int_{\Gamma_x\times\Gamma_t(\sigma)}
 f_N(x,t;u)\mathscr K_x(x)\mathscr K_{t,\sigma}(t)
 \,dx\wedge dt.                                         \tag{6}
\end{aligned}
\]

This follows by the residue theorem in either order. The sums are
finite and the contours are compact, so no limiting interchange is
involved. Formula (6) is an identity for the joint source before
either finite summation is estimated.

The central portion of the physical crossing trace is

\[
\frac{(-1)^d N C_{N,n}(\sigma)}{\sin(2\pi\sigma)}
 S_N(\sigma,u),
\qquad
C_{N,n}(\sigma)=
q^{\,n(d^2/4-\sigma^2/2)}.
                                                        \tag{7}
\]

It uses the original integer \(n\). At \(\sigma=0\), its removable
limit retains the normal derivatives at the double spectral roots.

## 3. Keep the lattice remainders on their original contours

Here is an exact finite expansion of (6), suitable for a subsequent
deformation. For \(\epsilon,\eta\in\{1,-1\}\), put

\[
\begin{aligned}
C_{\epsilon\eta}
&=(I+i\epsilon h_x)
  \times(J_\sigma+i\eta h_t),\\
E_\epsilon(x)&=e^{2\pi i\epsilon Nx},\\
D_\eta(t)&=
c_\sigma^{-\eta}e^{i\eta Nt},
\qquad
c_\sigma=(-1)^d e^{2\pi i\sigma}.
\end{aligned}
\]

On these horizontal sides, \(|E_\epsilon|=e^{-2\pi Nh_x}\) and
\(|D_\eta|=e^{-Nh_t}\). In the second equality the translation
\(\delta_\sigma\) cancels the factor \(e^{2\pi i\sigma}\)
exactly, including for complex \(\sigma\).

For integers \(P,L\geq0\), define

\[
W_P(z)=1+2\sum_{p=1}^{P}z^p,
\qquad
R_P(z)=\frac{2z^{P+1}}{1-z}.
\]

The cotangent kernels on the horizontal sides are exactly

\[
\mathscr K_x=-\epsilon i\pi N(W_P(E_\epsilon)+R_P(E_\epsilon)),
\]

\[
\mathscr K_{t,\sigma}
=-\eta\frac{iN}{2}(W_L(D_\eta)+R_L(D_\eta)).
\]

Let \(\mathcal V_N\) be the part of (6) on the twelve products
of sides for which at least one side is vertical, with their
original boundary orientations. Let \(\mathcal R_{P,L,N}\) be

\[
\frac{N^2}{8\pi}
\sum_{\epsilon,\eta}
\int_{C_{\epsilon\eta}} f_N
\left\{
 R_P(E_\epsilon)W_L(D_\eta)
 +W_P(E_\epsilon)R_L(D_\eta)
 +R_P(E_\epsilon)R_L(D_\eta)
\right\}\,dx\,dt,                                      \tag{8}
\]

where each horizontal rectangle is parametrized with both real
coordinates increasing. Put \(d_0=1\) and \(d_m=2\) for \(m>0\).
Then (6) becomes

\[
\begin{aligned}
S_N={}&\frac{N^2}{8\pi}
\sum_{\epsilon,\eta}
\sum_{p=0}^{P}\sum_{\ell=0}^{L}
d_p d_\ell c_\sigma^{-\eta\ell}
\int_{C_{\epsilon\eta}}
 f_N(x,t;u)
 e^{2\pi i\epsilon pNx+i\eta\ell Nt}\,dx\,dt\\
&+\mathcal R_{P,L,N}+\mathcal V_N.                       \tag{9}
\end{aligned}
\]

The constant \(N^2/(8\pi)\) includes the orientations of both
horizontal sides and the two residue kernels. In particular, the
four constant modes together have density \(N^2/(2\pi)\), the
product of the wire density \(N\) and trace density \(N/(2\pi)\).

Every term in (9) is retained. The omitted portions of the geometric
series are the explicit rational integrals (8), not an unspecified
error. Only finitely many modal integrals in (9) need be deformed.
The remainders and the vertical-side contributions stay on their
original contours until estimates for them are available. Moving an
infinite Fourier expansion onto a real boundary without a convergence
argument would not be justified by (9).

## 4. A simultaneous homotopy and its four connecting faces

Let \(F(x,t)\) be any one of the holomorphic modal integrands in
(9), including its exponential factor but excluding constant
coefficients. For real heights \(A,B\), define

\[
I(A,B)=
\int_a^b\int_{-T_N}^{T_N}
F(r+iA,v+\delta_\sigma+iB)\,dv\,dr.
\]

Suppose the straight simultaneous homotopy remains in its
holomorphy domain:

\[
(s,r,v)\longmapsto
(r+isA,\ v+\delta_\sigma+isB),
\qquad 0\leq s\leq1.                                  \tag{10}
\]

Differentiating under these compact integrals and integrating the
two spatial derivatives gives the exact identity

\[
I(A,B)-I(0,0)=Q_F(A,B),                                \tag{11}
\]

where

\[
\begin{aligned}
Q_F(A,B)={}&
iA\int_0^1\int_{-T_N}^{T_N}
\left[
F(b+isA,v+\delta_\sigma+isB)
-F(a+isA,v+\delta_\sigma+isB)
\right]\,dv\,ds\\
&+iB\int_0^1\int_a^b
\left[
F(r+isA,T_N+\delta_\sigma+isB)
-F(r+isA,-T_N+\delta_\sigma+isB)
\right]\,dr\,ds.
                                                        \tag{12}
\end{aligned}
\]

Equivalently, (11) is Stokes' theorem for the closed holomorphic
two-form \(F\,dx\wedge dt\) on the three-dimensional homotopy chain.
Its four swept boundary faces are precisely (12). There are no
additional two-dimensional corner faces in this simultaneous
homotopy.

For the selected positive-power, unit-charge mode,
\(p=0,\eta=-1,\ell=1\), take

\[
A=\Im x_n>0,\qquad B=\Im t_n<0.
\]

The connecting face at the positive cutoff is then exactly

\[
x=r+is\Im x_n,\qquad
t=T_N+\delta_\sigma+is\Im t_n.
                                                        \tag{13}
\]

Thus the face suggested by the numerical exploration is a legitimate
boundary face of a joint contour deformation. The other three
faces in (12) must accompany it.

To apply this directly to an original horizontal integral in (9),
use (11) twice:

\[
I(\epsilon h_x,\eta h_t)
=I(A,B)+Q_F(\epsilon h_x,\eta h_t)-Q_F(A,B).
                                                        \tag{14}
\]

Formula (14) moves finitely many holomorphic modal integrals to the
chosen joint contour. It does not move the cotangent poles. The
small-rectangle connecting faces, the new coupled faces, the
remainders (8), and the original vertical contributions all remain
explicit in the resulting identity.

## 5. The complete-meridian limit

Because \(f_N(x,-t;u)=-f_N(x,t;u)\) and
\(\tau_j(-\sigma)=-\tau_{d-j}(\sigma)\), the finite sum
\(S_N(\sigma,u)\) is odd in \(\sigma\). This proves the removability
in (7) directly for the central set of nodes.

Individual terms of a contour decomposition need not vanish at
\(\sigma=0\). If

\[
S_N(\sigma,u)=\sum_{\alpha} A_\alpha(\sigma,u)
\]

is the finite decomposition (9), with (14) inserted for any retained
modes, replace every summand by

\[
\operatorname{Odd}A_\alpha(\sigma,u)
=\frac{A_\alpha(\sigma,u)-A_\alpha(-\sigma,u)}2.
\]

The sum is unchanged, and each quotient
\(\operatorname{Odd}A_\alpha/\sin(2\pi\sigma)\) is holomorphic at
zero, with value \(\partial_\sigma A_\alpha(0,u)/(2\pi)\).
Contours depending on \(\sigma\) are parametrized as above; their
integrals are holomorphic while the common domain condition holds.
This gives a precise way of taking the Hermite limit without
discarding terms that cancel only after the full contour expression
is assembled.

## 6. What is now justified, and what still needs an estimate

The two finite sums have an exact joint residue representation.
Their selected modal integral can be moved along (10), and the
positive-cutoff face is (13). The canonical factorial supplies a
holomorphic exact integrand even when a denominator argument leaves
the usual positive factorial strip. The complete-meridian limit is
also retained.

What remains is quantitative: bound the four faces (12), the
vertical products in \(\mathcal V_N\), the explicit remainders
(8), and the retained competing modes below the selected
contribution. The negative-factorial continuation (5) may affect
those bounds. Neither holomorphy nor the homotopy identity proves
any required maximum inequality.
