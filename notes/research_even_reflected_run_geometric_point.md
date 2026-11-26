# The geometric point selected by an even reflected run

The unit-modulus point in
[the reflected growth theorem](research_even_run_sharp_reflected_growth.md)
solves the original two-terminal filling equations, with positive
original cells and the full primitive charges. This identifies its
geometric meaning. The
[spectral transgression proof](research_reflected_even_spectral_volume_transgression.md)
separately compares the integrated rate with the absolute geometric
action. Together these give the
[volume theorem for the original reflected knots](research_reflected_even_kashaev_volume_theorem.md).
The rate comparison is not inferred merely from a matching critical
equation.

## 1. The point and the original periods

Fix an integer \(k\ge2\). The reflected growth theorem, Lemma 2,
gives a unique pair \((\eta,\varphi)\) in the stated sector satisfying
\[
 \begin{split}
 &\eta>0,\qquad
       \frac{2\pi}{2k+1}<\varphi<\frac{\pi}{k},\\
 &\cosh(2k\eta)-\cos(2k\varphi)-\cosh\eta+\cos\varphi=0,\\
 &\sinh(2k\eta)\sinh\eta+\sin(2k\varphi)\sin\varphi=0.
 \end{split}
 \tag{1}
\]
Put
\[
 t=\varphi-i\eta,\qquad u=-\varphi-i\eta=-\overline t,
 \qquad
 r=ik t-\pi i=k\eta+i(k\varphi-\pi).
 \tag{2}
\]
The original edge variables are
\[
 a=\tan(t/2),\qquad b=\tan(u/2)=-\overline a,\qquad
                   q^2=1+a^2+b^2.
 \tag{3}
\]

**Theorem 1.** The square root \(q\) in (3) is positive real,
and all eight original edge shapes are positive. The original
principal returns are exactly
\[
 \begin{split}
 \operatorname{arsinh}(a\cos(u/2))
                         &=ik t-\pi i,\\
 \operatorname{arsinh}(b\cos(t/2))
                         &=-ik u-\pi i.
 \end{split}
 \tag{4}
\]
Thus they are the full primitive equations for the two original
terminal powers \(+2k,-2k\), respectively.

**Proof.** Introduce four nonnegative real quantities
\[
 P=\sinh^2(k\eta),\quad Q=\sin^2(k\varphi),\quad
 R=\sinh^2(\eta/2),\quad T=\sin^2(\varphi/2),
 \qquad D=1+R-T.
 \tag{5}
\]
Here \(P,R,T>0\), \(0<T<1/2\), and \(D>0\).
The first equation in (1) gives
\[
                         Q=R+T-P.
 \tag{6}
\]
Squaring the second equation in (1), and then using (6),
gives the exact factorization
\[
 \begin{split}
 0&=P(P+1)R(R+1)-Q(1-Q)T(1-T)\\
  &=(R+T)(P-T+1)
                  \{P(1+R-T)+RT+T^2-T\}.
 \end{split}
 \tag{7}
\]
The first two factors are strictly positive. Consequently
\[
 \begin{array}{ll}
 P=\dfrac{T(1-R-T)}D,&
 P+1=\dfrac{(1-T)(1+R+T)}D,\\[2mm]
 Q=\dfrac{R(1+R+T)}D,&
 1-Q=\dfrac{(1+R)(1-R-T)}D .
 \end{array}
 \tag{8}
\]
In particular \(R+T<1\).

All signs can now be checked before taking logarithms.
The angle \(k\varphi-\pi\) belongs to
\((-\pi/(2k+1),0)\). Hence
\[
 \begin{split}
 \cosh r&=\sqrt{(P+1)(1-Q)}-i\sqrt{PQ},\\
 \sinh r&=\sqrt{P(1-Q)}-i\sqrt{(P+1)Q}.
 \end{split}
 \tag{9}
\]
Also
\[
 \begin{split}
 \cos(u/2)&=\sqrt{(1-T)(1+R)}-i\sqrt{TR},\\
 a&=\frac{\sqrt{T(1-T)}-i\sqrt{R(1+R)}}D,\\
 q&=\frac{\sqrt{\,1-(R+T)^2\,}}D>0.
 \end{split}
 \tag{10}
\]
The last expression satisfies (3), by direct substitution.
Equations (8)--(10) prove both identities
\[
                  \sinh r=a\cos(u/2),\qquad
                  \cosh r=q\cos(u/2).
 \tag{11}
\]
For example the real and imaginary parts of either side of
the sinh identity are
\[
 \frac{\sqrt{T(1+R)}(1-R-T)}D,\qquad
        -\frac{\sqrt{R(1-T)}(1+R+T)}D .
 \]
Thus no sign of a square root was inferred from its square.
Since \(|\Im r|<\pi/2\), (11) gives the first principal
return in (4), with exactly the displayed logarithmic charge.
Complex conjugation and oddness of the principal arsinh
give the second return as \(-\overline r=-ik u-\pi i\).

It remains to check the strict positivity of the original
cells. The first equation of (1) implies
\[
       \cosh(2k\eta)-\cosh\eta
                    =\cos(2k\varphi)-\cos\varphi<1 .
 \tag{12}
\]
If \(\eta\ge1/2\), the left side is at least
\[
 \cosh2-\cosh(1/2)>
 \cosh2-\cosh1=2\sinh(3/2)\sinh(1/2)>3/2,
 \]
a contradiction. Therefore \(0<\eta<1/2\).
Because \(0<\varphi<\pi/2\),
\[
 |\Im a|=\frac{\sinh\eta}{\cosh\eta+\cos\varphi}
                   <\tanh\eta<\eta<\frac12 .
 \tag{13}
\]
As \(b=-\overline a\) and \(q>0\),
\[
 q^2-\{(\Re a)^2+(\Re b)^2\}
                      =1-2(\Im a)^2>\frac12 .
 \tag{14}
\]
This is precisely the
[original positive-edge criterion](research_positive_edge_global_monotonicity.md).
It proves positivity of all eight shapes. \(\square\)

## 2. The marked hyperbolic filling and its absolute action

Take the original ordered one-edge circle-tree exterior, with its
two terminal auxiliary circles, its original disk frames and
half-twist carriers. Use original integer filling coefficients
and carriers with
\[
                n_1=\eta_1-2p_1=2k,\qquad
                n_2=\eta_2-2p_2=-2k .
 \tag{15}
\]
For example the pure carriers \(\eta_1=\eta_2=0\) give
\(p_1=-k,p_2=k\). Theorem 1 does not change either primitive
basis or replace these powers by their unsigned magnitudes.

Both selected angles have imaginary part \(-\eta<0\).
The [pointwise marked-completion theorem](research_positive_point_marked_completion.md),
Theorem 1, now applies to (4) and (14).
It supplies the actual smooth hyperbolic filling of the
original two-terminal exterior, with both primitive filled
curves and all main cusps retained. The core lengths are
\(2\eta\).

In the original diagram this is the complement of
\[
                       K_k=C(R^{-2k}T(R^{2k})).
 \tag{16}
\]
It is a knot, not a two-component closure. In the endpoint
notation of
[the exact source-jet note, Section 6](research_two_run_monodromy_source_jets.md),
the even inner braid has the through pairing \(V=\{03,12\}\);
the physical turn changes it to \(H=\{01,23\}\); and the
even outer braid preserves \(H\). The outside cylindrical
arcs have pairing \(V\), so their union with \(H\) is one
cycle. The braid collars and the turn create no internal
closed component.

Let \(\psi(t,u)\) be the original edge phase, normalized by
\(\psi(0,0)=4G/\pi\), where \(G\) is Catalan's constant.
The absolute stationary action is
\[
 \mathcal G_k=
       \psi(t,u)+\frac{ik}{2\pi}(t^2-u^2)-i(t+u)
     =\psi(t,-\overline t)
                      +\frac{2k\varphi\eta}{\pi}-2\eta .
 \tag{17}
\]
The edge symmetries, or the real normalization and its
holomorphic continuation, give
\(\psi(t,-\overline t)\in\mathbb R\).
The volume of the marked filling is therefore
\[
       \operatorname{Vol}M_k
          =2\pi\mathcal G_k
          =2\pi\psi(t,-\overline t)
                        +4\eta(k\varphi-\pi).
 \tag{18}
\]
The constant in this formula is the complete original-cell
constant in the marked-completion theorem. It is not fixed
by a numerical comparison with a census manifold.

The source considered in the reflected growth theorem is the
original scalar
\(\phi_N(R^{-2k}T(R^{2k}))\).
Equations (17)--(18) identify a geometric action at its
proved unit-modulus point. The needed rate identity is
\[
                         2B_k(x_k)=\mathcal G_k .
 \tag{19}
\]
It is proved by the separate
[spectral transgression calculation](research_reflected_even_spectral_volume_transgression.md),
using the derivative and absolute limit recorded below.
Theorem 1 alone is not that integral comparison and does
not assert a free-boundary packet for this reflected source.

## 3. Differentiating the stationary action and fixing its limit

Use the smooth real-\(k\) continuation of (1) in the same
sector, established in the spectral transgression note.
All the algebra in Theorem 1 remains valid for real \(k\ge2\).
For noninteger \(k\), we use the stationary action (17);
we do not call it the volume of an integer Dehn filling.

The defining differential of the original edge phase is
\[
       \psi_t=-r_t/\pi,\qquad \psi_u=-r_u/\pi .
 \tag{20}
\]
By (4), the two partial derivatives in \(t,u\) of
\[
 W_k(t,u)=\psi(t,u)
                  +\frac{ik}{2\pi}(t^2-u^2)-i(t+u)
 \]
vanish at (2). The envelope derivative therefore has no
terms from \(t'(k)\) or \(u'(k)\):
\[
 \frac{d\mathcal G_k}{dk}
    =\frac{i}{2\pi}(t^2-u^2)
    =\frac{2\varphi\eta}{\pi},
 \qquad
 \frac d{dk}\{2\pi\mathcal G_k\}=4\varphi\eta .
 \tag{21}
\]
This uses the original powers \(+2k,-2k\), the original
unit charges in (4), and their original quadratic
coefficients. There is no rescaling of a meridian here.

The limit is also absolute. Equation (12) and
\(\eta<1/2\) give
\[
           \cosh(2k\eta)<1+\cosh(1/2).
 \]
Thus \(\eta=O(k^{-1})\), while
\(\varphi<\pi/k\). Hence \(t,u=O(k^{-1})\) and
\[
          k(t^2-u^2)\longrightarrow0,\qquad
          t+u\longrightarrow0.
 \]
The normalization of the same edge phase gives
\[
        \lim_{k\to\infty}\mathcal G_k=\frac{4G}{\pi},
       \qquad
        \lim_{k\to\infty}2\pi\mathcal G_k=8G.
 \tag{22}
\]
The spectral transgression proof gives the same derivative
and the limit \(8G\) for \(4\pi B_k(x_k)\) on this
real-parameter continuation. Subtracting the two functions
and using (22) proves (19), with no undetermined additive
constant.

## 4. The original invariant normalization

Let
\[
                \mathcal E_{k,N}
                    =\phi_N(R^{-2k}T(R^{2k})).
 \tag{23}
\]
This is the entire original scalar, with the exact physical
crossings, turn, reduced cap, and full Newton quotient.
The reflected growth theorem identifies it exactly with
\(\sum_j |(M^{2k}e_0)_j|^2\).
The equality is supplied by the actual reflected pairing,
not by taking absolute values inside a different signed sum.

The original normalization theorem,
[Finite spectral evaluation and uniform filling bounds,
Theorem 10.1](../papers/filling-bounds/sections/diagram-evaluation.tex),
and the exact closing formula
\(\mathrm{mt:closing}\) in
[the meridian-tangle paper](../papers/meridian-tangles/main.tex)
give, for \(N\ge3\),
\[
        K_N(K_k)=\zeta_{N,K_k}\mathcal E_{k,N},
                         \qquad |\zeta_{N,K_k}|=1 .
 \tag{24}
\]
The character is the integer framing correction of the
literal original diagram. Its writhe is not being guessed
from the opposite signs of the two algebraic powers.
There is exactly one reduced cut, with unknot value one.
No additional factor of \(N\), quantum dimension, or
auxiliary-circle normalization is introduced.

Consequently the proved action identity (19), together
with the sharp growth theorem, gives the reduced Kashaev
volume identity for the actual knots (16), through both
level parities. The
[assembled theorem](research_reflected_even_kashaev_volume_theorem.md)
records this conclusion. Equations (21)--(24) supply its
geometric and normalization inputs.
