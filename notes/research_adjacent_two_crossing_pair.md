# Two adjacent two-crossing fillings with one boundary left open

Research calculation and geometric lemma, 2 November 2026. Consider
the three-vertex path with powers \(2,2,n\), where the last power is
not yet filled. This note gives an exact factorial formula for the
polynomial left by the first two traces. It has a regular
two-variable critical point. Independently, an explicit positive
cone deformation identifies the geometric critical point for the
same original primitive fillings.

The note does not prove a global asymptotic for the finite double
sum. In particular, finding the regular critical point does not
prove that its contribution survives the full discrete contraction.
The complete asymptotic is now proved in the separate
[boundary theorem](research_adjacent_two_crossing_boundary_theorem.md),
using the exact full-period contour. The manuscripts remain frozen.

## 1. An exact composition formula

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Let \(e_j\), \(R\), and \(\phi_N\) be the original Newton basis,
physical crossing, and complete closing functional. Set
\[
 F_j=(Q;Q)_j,\qquad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad F_0=S_0=1.
 \tag{1}
\]
All the products in a denominator below have index less than \(N\).
The trace is taken in the full quotient algebra, including its
first normal derivatives at repeated spectral roots.

Write
\[
 K_N(s,t)=\sum_{j=0}^{D}e_j(-2\cos s)e_j(-2\cos t),
 \qquad \mathcal D_{n,N}f=\phi_N(R^nf).
\]
After fixing the two adjacent powers at two, the remaining
boundary polynomial is
\[
 Z_N(u)=\mathcal D_{2,N}^{(t)}
               [H_{2,N}(t)K_N(t,u)],
 \qquad H_{2,N}(t)=\mathcal D_{2,N}^{(s)}K_N(s,t).
 \tag{2}
\]

**Proposition 1.** At every integer level,
\[
 \boxed{
 Z_N(u)=N^2
   \sum_{\substack{i,j\ge0\\i+j<N}}
       q^{\,i^2+(i-j)^2}
       \frac{F_{i+j}}{F_i^3F_j^2}\,
       e_j(-2\cos u).}
 \tag{3}
\]
This is an identity for the entire boundary polynomial.

**Proof.** The [two-crossing leaf identity](research_two_crossing_terminal_filling.md)
and \(S_i=i^i q^{-i(i+1)/2}F_i\) give
\[
 H_{2,N}(t)=N\sum_{i=0}^{D}\frac{q^{i^2}}{F_i}e_i(-2\cos t).
\]
The [two-boundary trace identity](research_degree_two_power_two_formula.md)
is
\[
 \phi_N(R^2e_i e_j)
   =Nq^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2},
\]
with zero coefficient when \(i+j\ge N\). Substitute both identities
in (2). Both were proved in the full algebra, so the substitution
has not replaced the trace by evaluations at its distinct roots.
QED.

For fixed \(j\), the inner coefficient can also be written as
\[
 \frac{N^2q^{j^2}}{F_j}
 \sum_{i=0}^{D-j}
    Q^{i^2-ij}\frac{(Q^{j+1};Q)_i}{(Q;Q)_i^3}.
 \tag{4}
\]
This is a terminating basic hypergeometric sum. Formula (4) alone
does not assert a product evaluation or remove its oscillation.
The two-variable formula (3) is sufficient for the local calculation.

## 2. The regular factorial phase

Let
\[
 J(z)=\int_0^z\log(2\sin\pi w)\,dw
\]
on the branch continued from \(0<z<1\), and let \(b(x,u)\)
be the canonical Newton phase, so that
\[
 b(x,0)=J(2x)-4J(x).
\]
These functions and the factorial interpolation are defined in the
[two-crossing boundary calculation](research_two_crossing_terminal_filling.md).
For \(x=i/N,\ y=j/N\), the phase of (3) is
\[
 \begin{aligned}
 W(x,y;u)={}&J(x+y)-3J(x)-2J(y)+b(y,u)\\
            &+i\pi(x^2-xy+y^2/2+x+y/2).
 \end{aligned}
 \tag{5}
\]
On compact sets where its factorial arguments remain in their
regular strips, the individual summand is
\[
 N^{-1}a(x,y)e^{NW(x,y;u)}(1+O(N^{-1})),
 \tag{6}
\]
with
\[
 a(x,y)=\frac18 e^{-i\pi(x+y/2)}
       \frac{\sqrt{\sin\pi(x+y)}}
            {(\sin\pi x)^{3/2}(\sin\pi y)^2}.
 \tag{7}
\]
The roots continue from the positive real factorial interval.
Indeed the exact coefficient in (3) is
\[
 N^2 i^{\,2i+j}
 q^{\,i^2-ij+j^2/2-i-j/2}
       \frac{S_{i+j}}{S_i^3S_j^2}.
\]
The factorial square-root factors contribute \(1/4\), and the
Newton factor contributes \(1/(2N\sin\pi y)\). This gives (6)--(7),
including the midpoint shifts.

**Proposition 2.** At \(u=0\), the following point is critical for
the unexponentiated phase (5):
\[
 X=e^{2\pi ix_*}=\frac{5+i\sqrt7}{16},
 \qquad
 Y=e^{2\pi iy_*}=\frac{i}{\sqrt7},
 \qquad
 x_*=\frac{\log X}{2\pi i},\quad
 y_*=\frac{\log Y}{2\pi i}.
 \tag{8}
\]
The logarithms have arguments between zero and \(\pi\). In
particular,
\[
 0<\Re x_*<\frac14,\qquad
 \Re y_*=\frac14,\qquad
 0<\Re(x_*+y_*)<\frac12,
\]
and both imaginary parts are positive. Thus every factorial
argument in (5)--(7), including the numerator arguments in
\(b(y,0)\), lies in a regular strip.

**Proof.** Exponentiating the two critical equations gives
\[
 Y(3X^2-3X+1)=X^2,
 \qquad
 Y(XY-1)(Y+1)^2=X(Y-1)^4.
 \tag{9}
\]
Their resultant in \(Y\) is
\[
 -X(X-1)^3(8X^2-5X+1).
\]
The root (8) satisfies (9). This checks the algebraic equations,
but not yet their logarithmic lifts. To check the latter, write
the actual derivatives:
\[
 \begin{aligned}
 W_x={}&\log(2\sin\pi(x+y))-3\log(2\sin\pi x)
                         +i\pi(2x-y+1),\\
 W_y={}&\log(2\sin\pi(x+y))-6\log(2\sin\pi y)
            +2\log(2\sin2\pi y)+i\pi(-x+y+1/2).
 \end{aligned}
 \tag{10}
\]
At (8), all the sine arguments in these logarithms have positive
real part. Their arguments are consequently the ones in
\((-\pi/2,\pi/2)\), continued from the real strips. Substitution
in (9) shows that each derivative is an integer multiple of
\(2\pi i\). For the first derivative its imaginary part lies
strictly between \(-3\pi/4\) and \(7\pi/4\): the sine arguments
are between zero and \(\pi/2\), while
\(\pi(2\Re x_*-\Re y_*+1)\) lies between \(3\pi/4\)
and \(5\pi/4\). For the second derivative,
\(0<\arg\sin(\pi y_*)<\pi/4\) and
\(\arg\sin(2\pi y_*)=0\). Its imaginary part lies between
\(-\pi\) and \(5\pi/4\). Hence both integer multiples are
zero.

The exact Hessian is
\[
 W''(x_*,y_*;0)=\frac{\pi}{64}
 \begin{pmatrix}
 -43\sqrt7+409i&5\sqrt7-119i\\
 5\sqrt7-119i&-91\sqrt7+105i
 \end{pmatrix}.
 \tag{11}
\]
Its real part is negative definite, since \(43\cdot91-25>0\).
Its determinant is
\[
 -\frac{\pi^2}{128}(49+1267\sqrt7\,i)\ne0.
 \tag{12}
\]
This also proves the holomorphic continuation of the critical point
for small complex \(u\). QED.

If a complete contour argument justifies this critical contribution,
the \(N^{-1}\) summand, two lattice factors \(N^2\), and
two-dimensional Gaussian factor \(N^{-1}\) give power \(N^0\).
The candidate leading coefficient is
\[
 \frac{2\pi a(x_*,y_*)}
      {\sqrt{\det[-W''(x_*,y_*;0)]}},
 \tag{13}
\]
with its square root fixed by the actual integration contour.
Neither (13) nor Proposition 2 is a global asymptotic theorem.
The stationary boundary Hessian is already exact:
\[
 \frac{d^2}{du^2}\operatorname{stat}_{x,y}W(x,y;u)
       \bigg|_{u=0}
   =-\frac{\tan(\pi y_*)}{2\pi}
   =-\frac{\sqrt7+3i}{8\pi}.
 \tag{13a}
\]
The mixed derivatives with \(u\) vanish at zero because the
Newton phase is even in \(u\).

## 3. The original geometric equations

Let \(s\) be the angle at the selected original leaf, \(t\)
the angle at the selected middle vertex, and \(u=0\) the complete
remaining boundary. The marked geometric action is
\[
 \mathcal A(s,t)=\psi(s,t)+\psi(t,0)
           +\frac{i}{2\pi}(s^2+t^2)-i(s+t),
 \tag{14}
\]
where
\[
 \psi_s(s,t)=-\frac1\pi\operatorname{arsinh}
                       (\tan(s/2)\cos(t/2)),\qquad
 \psi(0,0)=v_{\rm oct}/\pi.
\]
Both original powers are \(2\), with carrier zero and surgery
coefficient \(-1\). The original slopes are therefore
\(\mu_s-\lambda_s\) and \(\mu_t-\lambda_t\), in their
respective disk frames.

The following path keeps these primitive curves. First fill the
leaf to charge one with \(t=0\), using the positive cone path
already proved in the
[terminal geometry](research_verified_terminal_fillings_and_long_remainder.md).
Next keep that charge fixed, and increase the middle charge from
zero to one.

**Proposition 3.** The second stage has the explicit solution
\[
 \begin{gathered}
 0\le\theta\le\pi/3,\qquad
 r=\sin\theta,\qquad b=\operatorname{arsinh}r,\\
 t=2\theta-2ib,\qquad
 \cos s=-1+i\cos(t/2),\qquad
 \pi/2<\Re s<\pi,\quad \Im s<0.
 \end{gathered}
 \tag{15}
\]
It satisfies the full logarithmic equations
\[
 \psi_s(s,t)+\frac{is}{\pi}=i,\qquad
 \psi_t(s,t)+\psi_t(t,0)+\frac{it}{\pi}
                              =\frac{3i\theta}{\pi}.
 \tag{16}
\]
All sixteen original tetrahedra in the two edge blocks remain
positive on the concatenated path. At its endpoint,
\[
 \begin{gathered}
 t_*=\frac{2\pi}{3}-i\operatorname{arcosh}(5/2),
 \qquad \cos(t_*/2)=\frac{\sqrt7+3i}{4},\\
 \cos s_*=-\frac74+\frac{i\sqrt7}{4}.
 \end{gathered}
 \tag{17}
\]

**Proof of the equations.** Put \(S=s/2\), \(T=t/2\),
and \(C=\cos T\). Along (15),
\[
 C=\sqrt{1-r^4}+ir^2,\qquad |C|=1,\quad \Re C>0,
 \qquad \cos^2 S=iC/2.
 \tag{18}
\]
The root \(\cos S\) is chosen in the first quadrant. It follows
that
\[
 \tan S\,C=-i\sin s,\qquad
 \tan T\cos S=r.
\]
For the second equality, squaring gives
\[
 (\tan T\cos S)^2=\frac{i}{2}(C^{-1}-C)=r^2,
\]
and the sign is positive near \(\theta=0\), hence throughout.
Define
\[
 R_s=\exp\operatorname{arsinh}(\tan S\cos T),\qquad
 R_t=\exp\operatorname{arsinh}(\tan T\cos S).
\]
The continued logarithms are
\[
 \log R_s=i(s-\pi),\qquad \log R_t=b.
 \tag{19}
\]
Indeed \(i(s-\pi)\) has positive real part and imaginary part
in \((-\pi/2,0)\), the corresponding branch of \(\operatorname{arsinh}\).
Also
\[
 \log(\sec T+\tan T)=b-i\theta.
 \tag{20}
\]
For example, (20) follows from the explicit formula for
\(\sec(a-ib)+\tan(a-ib)\), using \(\sinh b=\sin a\)
with \(a=\theta\). Equations (19)--(20) give (16) directly.
They are equalities of logarithms, not only of multipliers.

**Proof of positivity.** For a general edge with half-angles
\(S,T\), the eight ordered shapes in the original two-octahedron
construction simplify to
\[
 (A,B,-1/A,-1/B),\qquad(C_1,D_1,-1/C_1,-1/D_1),
 \tag{21}
\]
where
\[
 A=iR_s e^{-iT},\quad B=i e^{iS}/R_t,\quad
 C_1=i e^{-iT}/R_s,\quad D_1=i e^{iS}R_t.
 \tag{22}
\]
These are obtained from the original ordered cross ratios, not
by changing the triangulation. One direct verification writes
\(y=\tan S,\ z=\tan T,\ p=\sqrt{1+y^2+z^2}\).
The equatorial coordinate is \((1+z^2)/(p^2+1)\); the two pairs
of apices simplify to
\[
 \left(\frac{p+y}{p-i},\frac{z-i}{p-i}\right),\qquad
 \left(\frac{p+y}{p+i},\frac{z+i}{p+i}\right).
\]
Substitute these in the ordered cross ratios of the
[geometric paper](../papers/circle-tree-geometry/main.tex).
The four initial shapes become
\[
 \frac{p+y}{z-i},\quad-\frac{y-i}{p+z},\quad
 \frac{z+i}{p+y},\quad-\frac{p+z}{y+i},
\]
which are exactly (22).

In (15), \(R_t=e^b>0\). Thus \(B,D_1\) have positive
imaginary part because \(0<\Re S<\pi/2\).
Write \(\alpha=\Re s\), \(H=-\Im s>0\).
The only additional inequality needed for \(A,C_1\) is
\[
 \alpha>\pi/2+\theta.
 \tag{23}
\]
To prove it, the real and imaginary parts of (18) give
\[
 \cos\alpha\cosh H=-(1+r^2),\qquad
 \sin\alpha\sinh H=\sqrt{1-r^4}.
\]
Consequently
\[
 \sinh^2H=\frac{1+2r^2+\sqrt{5+4r^2}}2>r^2.
 \tag{24}
\]
Since \(\alpha\in(\pi/2,\pi)\), comparison of cotangents
shows that (24) is equivalent to
\[
 -\cot\alpha
  =\sqrt{\frac{1+r^2}{1-r^2}}\tanh H
  >\frac{r}{\sqrt{1-r^2}}=\tan\theta,
\]
which proves (23). The arguments of the factors multiplying \(i\)
in \(A,C_1\) are \(\alpha-\pi-\theta\) and
\(\pi-\alpha-\theta\); both lie in \((-\pi/2,\pi/2)\).
Their imaginary shape parts are therefore positive. The operation
\(z\mapsto-1/z\) preserves the upper half-plane, so all eight
shapes in (21) are positive.

The rational coordinates have no singular denominator on this
path. In fact
\[
 p=\frac{\cosh b}{\cos S},\qquad
 p^2+1=\frac{1-2iC}{C^2},
\]
and \(C,\cos S,p\) are nonzero. The real part of \(1-2iC\)
is \(1+2r^2>0\). The factors \(p\pm y,p\pm z\) are nonzero
because their paired products are respectively \(1+z^2\)
and \(1+y^2\). Thus the same original face formulas continue
along the path.

For the second edge, whose angles are \(t,0\), positivity follows
from the [isolated-edge shapes](research_isolated_internal_vertex_geometry.md):
\(e^{it/2}\) and \(\sec(t/2)+\tan(t/2)\) have positive real
parts. Positivity on the first stage was already established by
the terminal cone path. This proves the proposition. QED.

## 4. Primitive periods and the absolute geometric action

The face identifications are the original ones, continued without
singularity through Proposition 3. Their winding integers start
at the complete structure and remain constant. The primitive
period formulas of the geometric paper therefore turn (16) into
cone angles \(2\pi\) and \(6\theta\) at the two selected
original auxiliary curves. The unfilled boundary cusp remains
complete because its derivative \(\psi_u(t,0)\) vanishes.
The main cusps remain complete under the same original face maps.

The second stage has the stationary action
\[
 \mathcal A_\lambda
  =\operatorname{stat}_{s,t}
   \left[\psi(s,t)+\psi(t,0)
       +\frac{i}{2\pi}(s^2+t^2)-is-i\lambda t\right],
 \qquad \lambda=3\theta/\pi.
 \tag{25}
\]
Its derivative has real part \(\Im t\). Schläfli's formula
has the same derivative after multiplication by \(2\pi\).
The first stage starts with four original regular ideal octahedra
and has the already fixed terminal volume constant. Concatenating
the two stages therefore gives the absolute identity
\[
 \operatorname{Vol}(Y_{2,2})
                =2\pi\Re\mathcal A(s_*,t_*),
 \tag{26}
\]
where \(Y_{2,2}\) is the original partially filled exterior with
the last auxiliary cusp left complete. This is a geometric
statement, independent of a quantum asymptotic.

For later comparison, eliminating the leaf along this path gives
\[
 G_{\rm leaf}(t)=\frac12\psi(t,0)
                      -\frac{it^2}{8\pi}-\frac{3i\pi}{8},
\]
with the constant fixed at \(t=0\) by the proved leaf calculation.
Thus (25) equals
\[
 \frac32\psi(t,0)+\frac{3it^2}{8\pi}
                         -i\lambda t-\frac{3i\pi}{8}.
 \tag{27}
\]
Both constituent implicit equations are nondegenerate: the leaf
Hessian is
\[
 \frac{i}{\pi}-\frac1{2\pi\cos S\cosh b},
\]
and its Schur complement in the full selected Hessian is
\[
 \frac{3}{4\pi}\bigl(-\sec T+i\bigr).
\]
Each has negative real part. The geometric action hence continues
holomorphically in the remaining boundary angle \(u\) near zero.
Its boundary Hessian at the final point is
\[
 -\frac{\cos(t_*/2)}{2\pi}
                  =-\frac{\sqrt7+3i}{8\pi}.
 \tag{28}
\]

## 5. Comparison of the two actions, with all logarithms fixed

The finite chart and the original geometric equations select the
same algebraic central angle:
\[
 2\cos t_*=-X^{-1}-Y^{-1}
                    =-\frac52+\frac{3i\sqrt7}{2}.
 \tag{29}
\]
Equations (8) and (17) verify this equality exactly. To determine
the additive constant, write
\[
 \begin{aligned}
 W_0(x,y)&=J(x+y)-2J(x)-2J(y)
                 +\frac{i\pi}{2}((x-y)^2+x+y),\\
 L(x)&=-J(x)+\frac{i\pi}{2}(x^2+x).
 \end{aligned}
 \tag{30}
\]
Then \(W=W_0+L(x)+b(y,u)\).

**Proposition 4.** Let \(\mathcal G(u)\) be the stationary
geometric action with the remaining angle \(u\), continued from
Proposition 3. On a complex neighborhood of zero,
\[
 \operatorname{stat}_{x,y}W(x,y;u)=\mathcal G(u)+i\pi.
 \tag{31}
\]
Thus the exact action difference corresponds to the scalar
\(e^{i\pi N}=(-1)^N\), independently of the diagram framing.

**Proof.** The
[two-boundary phase comparison](research_degree_two_power_two_geometric_phase.md)
proves the local identity
\[
 W_0(x,y)=b(x,t)+b(y,t)+\frac{it^2}{2\pi}-it+\frac{i\pi}{2},
 \qquad 2\cos t=-X^{-1}-Y^{-1},
 \tag{32}
\]
near \(x=y=z_0=1/4+i\log3/(4\pi)\). It proves the constant
with the original logarithms, including
\[
 b_t(x,t)+b_t(y,t)+it/\pi-i=0.
 \tag{33}
\]
We first continue this identity to (8), specifying a path which
cannot alter those logarithms.

Take the straight segment from \((z_0,z_0)\) to \((x_*,y_*)\).
On it both \(x,y\) have real part between zero and one half and
positive imaginary part. Write \(A=|X^{-1}|\), \(B=|Y^{-1}|\).
Then
\[
 \sqrt3\le A,B\le2\sqrt2,
 \qquad
 \cos(\arg X^{-1}-\arg Y^{-1})>7/16.
\]
For instance the largest angular separation is the final one,
whose cosine is \(\sqrt{14}/8>7/16\). Consequently
\[
 |X^{-1}+Y^{-1}|^2-(A+1)^2
   >2-\frac{13A}{24}>0,
\]
where we used \(B\ge\sqrt3>5/3\) and \(A<3\).
The same inequality holds with \(A,B\) interchanged.

Choose \(0<\Re t<\pi,\ \Im t<0\) in (32); this is the
unique such branch since the right side has positive imaginary
part. Put \(T=e^{it}\). The relation
\(T+T^{-1}=-(X^{-1}+Y^{-1})\) gives
\[
 |T|>|X^{-1}+Y^{-1}|-1>\max(A,B).
 \tag{34}
\]
It follows that both
\[
 1/2-x-t/(2\pi),\qquad 1/2-y-t/(2\pi)
\]
stay in the upper half-plane. The other two denominator arguments
\(1/2-x+t/(2\pi)\), \(1/2-y+t/(2\pi)\) have real parts
strictly between zero and one; so do the numerator arguments
\(1/2\pm t/(2\pi)\). All remaining factorial arguments are
in their original strips. The factorial expression
\[
 b(x,t)=J(1/2+t/(2\pi))+J(1/2-t/(2\pi))
       -J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x)
 \tag{35}
\]
therefore continues without a zero or a logarithmic winding on
this path. Formula (32), including its constant, holds at (8)
and on a neighborhood of it.

It remains to compare these branches with the original geometric
path (15). Its leaf critical wire and its remaining-edge critical
wire are explicitly
\[
 X_{\rm leaf}(t)=\frac1{1-2iC},\qquad
 Y_{\rm edge}(t)=\frac{1+iC}{1-iC},
 \qquad C=\cos(t/2).
 \tag{36}
\]
At the endpoint they are exactly \(X,Y\) in (8).
The leaf wire has \(0<\Re x<1/4\). For
\(\theta\le\pi/4\) this puts both its denominator arguments
in (35) in \(0<\Re<1\). For \(\theta\ge\pi/4\),
\[
 \arg X_{\rm leaf}
  =\arctan\frac{2\sqrt{1-r^4}}{1+2r^2}<\pi/4,
\]
so \(\Re x<1/8\); now
\(1/2-\Re x-\theta/\pi>1/24\).
Thus both leaf denominator arguments remain in the same regular
strip throughout.

For the other edge, (18) gives
\[
 Y_{\rm edge}=i\sqrt{\frac{1-r^2}{1+r^2}},\qquad
 y=\frac14+\frac{i}{2\pi}\operatorname{artanh}(r^2).
\]
Its potentially troublesome denominator has imaginary part
\[
 \Im\{1/2-y-t/(2\pi)\}
 =\frac{2\operatorname{arsinh}r-\operatorname{artanh}(r^2)}
        {2\pi}>0\quad(r>0).
 \tag{37}
\]
To prove the inequality, compare the hyperbolic tangents of
the two positive terms. Squaring the resulting positive sides
reduces it to
\[
 4+3r^2-4r^4-4r^6>0.
\]
For \(r^2\le3/4\), its left side is at least \(1/16\).
At \(r=0\) the denominator argument is \(1/4\); afterwards it
can cross the imaginary axis only through the upper half-plane.
Every other argument remains in a regular strip.
The branches reached by (15) therefore agree with those fixed by
(34)--(35), including the upper continuation in (37).

On these branches the established leaf phase identity continues
from \(t=0\):
\[
 \operatorname{stat}_x[b(x,t)+L(x)]
                         =G_{\rm leaf}(t)+i\pi/2.
 \tag{38}
\]
The edge identity likewise continues from its complete end:
\[
 \operatorname{stat}_y[b(y,t)+b(y,u)]=\psi(t,u).
 \tag{39}
\]
These are local phase identities; no assertion about an entire
finite sum along this continuation is needed.

Now substitute (38)--(39) into (32). The \(x,y\) critical
equations for \(W\) become the leaf and edge wire equations,
and (33) becomes the original middle filling equation.
The resulting stationary action is
\[
 G_{\rm leaf}(t)+\psi(t,u)+\frac{it^2}{2\pi}-it+i\pi.
\]
Its first four terms are exactly the original geometric action
with the leaf eliminated. The nonzero Hessians proved above
identify the corresponding nearby holomorphic critical branches.
This proves (31), with no omitted constant or boundary-dependent
phase. QED.

## 6. The complete quantum asymptotic

The [boundary theorem](research_adjacent_two_crossing_boundary_theorem.md)
now proves the asymptotic for the whole original polynomial, with a
nonzero holomorphic leading coefficient, full real-angle decay, and
a Gaussian complex-strip estimate. Its phase and geometric
normalization are exactly those calculated in this note.

The proof first discards the already bounded extreme second indices.
It then extends the triangular sum to a rectangle: every added
lattice term is exactly zero. The lower first-variable contour
becomes a complete circle. Its exact cyclotomic normalization gives
a holomorphic differential, and the error of restoring the original
normalization is exponentially small. The two vertical sides are
combined by the original translation multiplier, with the peripheral
factor retained. Written endpoint estimates and an interval
certificate bound all remaining contour terms below the selected
rate. The horizontal maximum and local Gaussian expansion finish
the argument.

This closes the adjacent \((2,2)\) source calculation and permits
further sufficiently long fillings of its free boundary. It does
not prove the finite-exception statement for the entire
three-parameter family: arbitrary adjacent short powers remain a
separate requirement. The earlier triangular-contour and arc notes
are retained as valid intermediate calculations.

## 7. Finite checks and asymptotic diagnostics

Run

    python3 experiments/check_adjacent_two_crossing_source.py

The [saved output](../repro/results/research-adjacent-two-crossing-source.json)
includes exact cyclotomic coefficient comparisons with the original
crossing matrix through level ten. It also evaluates the entire
finite double sum and compares it with the candidate critical
contribution at several even and odd levels. Those comparisons
are consistent with a relative \(O(N^{-1})\) correction.
They check the finite normalization and provide a diagnostic for
the contour theorem. The proof of the global asymptotic is in
Section 6 and its linked boundary theorem; the finite evaluations
are checks of normalization, not that proof.
