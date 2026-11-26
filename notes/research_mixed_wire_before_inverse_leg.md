# Original wires precede their inverse legs on every positive path

Research theorem, 5 November 2026. The actual positive charge equations
put each original wire strictly before each incident inverse leg in
real index. The proof combines two fixed exact polynomial positivity
certificates with a half-plane calculation. It uses no critical-root
search or numerical parameter cover.

## 1. A uniform bound for the original wire cotangent

Use the positive path family with all integer powers at least three
and original incidence degree at most two. At an active vertex write
\(\tau=a-iH\), \(C=\cosh H\), \(c=\cos a\), and
\(A=\cos^2(\tau/2)\). Complete vertices have \(A=1\).
The [cosine phase maximum principle](research_geometric_phase_maximum_principle.md)
gives
\[
 C<7/4,\qquad
 a<2\pi/3+\tfrac19\sin a,\qquad
 \tan\arg\cos(\tau/2)<1/\sqrt2.                        \tag{1}
\]
The [general sine-lens theorem](research_mixed_all_leg_half_plane.md)
gives \(|A|<1\), \(|1-A|<1\) at active vertices, and fixes
every inverse leg in the lower half-plane.

First, every actual \((C,c)\) lies in the union of the two rectangles
\[
 [1,6/5]\times[-3/5,1],\qquad
 [6/5,7/4]\times[-1/2,1].                               \tag{2}
\]
Indeed if \(a\ge2\pi/3\), then
\(0\le a-2\pi/3<\sqrt3/18\). Convexity of cosine on
\([2\pi/3,\pi]\) gives
\(c>-1/2-1/12=-7/12>-3/5\).
If also \(C\ge6/5\), then
\[
 \left(\frac{\sinh H}{\sin a}\right)^2
 \ge\frac{44}{75}>\frac12.                             \tag{3}
\]
Each original return therefore has negative imaginary part: the
argument of \(\tan(\tau/2)\) is
\(-\arctan(\sinh H/\sin a)\), and every neighboring cosine
has tangent of its argument less than \(1/\sqrt2\).
The imaginary period would give
\(a<2\pi\chi/n\le2\pi/3\), a contradiction. Thus
\(c>-1/2\) when \(C\ge6/5\), proving (2).

Write \(\alpha=A^{-1}=u-iv\). The lens and the phase bound imply
\[
 u>1/2,\qquad v\ge0,\qquad v<\kappa u,
 \qquad\kappa=2\sqrt2.                                 \tag{4}
\]
The explicit real and imaginary parts satisfy
\[
 u=\frac{2(1+Cc)}{(C+c)^2},\qquad
 v^2=\frac{4(C^2-1)(1-c^2)}{(C+c)^4}.                   \tag{5}
\]
These formulas include complete vertices. The denominators are
strictly positive on both rectangles (2).

Define the polynomial
\[
 P(C,c)=144(1+Cc)(C+c)^2+45(C+c)^4
                              -64(C^2-1)(1-c^2).        \tag{6}
\]
After affine rescaling of either rectangle to \([0,1]^2\),
all 25 tensor Bernstein coefficients of bidegree \((4,4)\)
are positive. Their exact minima are respectively
\[
                    \frac{1453}{625},\qquad
                    \frac{67179}{4000}.                \tag{7}
\]
The dedicated checker reconstructs every coefficient rationally,
checks the polynomial identities, and stores both full tables in
its result. Since the Bernstein basis is nonnegative and sums to
one, (7) proves \(P>0\) on the two whole rectangles, rather
than on a sample of points.

Equations (5)--(7) give
\[
 v^2<\tfrac92u+\tfrac{45}{16},\qquad
 |2\alpha-1|-\Re(2\alpha-1)<\tfrac92.                  \tag{8}
\]
For the second inequality square the positive quantity
\(2u-1+9/2\); its squared excess over \(|2\alpha-1|^2\)
is \(18u+45/4-4v^2>0\).

On an edge put \(\beta=B^{-1}\) and take the original root
\[
 q=p-ih,\qquad q^2=\alpha+\beta-1.                     \tag{9}
\]
Both inverse cosine squares have real part greater than one half,
so the original square root has \(p>h\ge0\). Applying (8)
at both ends and using the triangle inequality gives
\[
 2h^2=|q^2|-\Re q^2
 \le\tfrac12\sum_{\gamma\in\{\alpha,\beta\}}
        \bigl(|2\gamma-1|-\Re(2\gamma-1)\bigr)
 <\tfrac92,
 \qquad h<\tfrac32.                                   \tag{10}
\]

## 2. The phase-constrained half-plane calculation

Write \(\alpha=u-iv\), \(\beta=s-it\), with (4) at both
ends, and set
\[
 T=p^2-h^2+1=u+s,\quad L=2ph=v+t,\quad
 D=p^2+(h-1)^2.                                        \tag{11}
\]
Thus
\[
 \tfrac12<u<T-\tfrac12,\qquad
 \max\{0,L-\kappa(T-u)\}\le v\le\min\{L,\kappa u\},
 \qquad L<\kappa T.                                    \tag{12}
\]
The non-strict signs in the displayed interval only enlarge the
actual strict phase constraints.

**Lemma 1.** If \(p>h\ge0\), \(h<3/2\), and (12) holds,
then
\[
 N=p u(D-u)+(1+h)Dv-pv^2>0.                             \tag{13}
\]

*Proof.* The function is concave in \((u,v)\). For \(0\le h\le1\),
use the larger rectangle
\([1/2,T-1/2]\times[0,L]\). Its four corner values, in order
\((1/2,0),(T-1/2,0),(1/2,L),(T-1/2,L)\), are
\[
\begin{split}
 &\tfrac p4(2h^2-4h+2p^2+1),\\
 &\tfrac p4(2h-1)^2(2p^2-2h^2+1),\\
 &\tfrac p4(2p^2-2h^2+1)(-4h^2+4h+1),\\
 &\tfrac p4(2p^2-6h^2+4h+1).
\end{split}                                                   \tag{14}
\]
The first, third and fourth are strictly positive because \(p>h\).
The second is nonnegative. Concavity and the strict interval for
\(u\) prove (13), including \(h=1/2\) and the degenerate
\(L=0\) case.

Now let \(1\le h<3/2\). For each fixed \(u\), concavity
in \(v\) reduces the minimum to the four possible boundary
pieces \(v=0\), \(v=L\), \(v=\kappa u\), and
\(v=L-\kappa(T-u)\).

On \(v=0\), one has
\(D-u>D-T+1/2=(2h-1)^2/2>0\).
On \(v=\kappa u\), the quotient \(N/u\) decreases affinely
in \(u\); feasibility gives \(u\le L/\kappa\).
At its upper endpoint the exact value is
\[
 N(L/\kappa,L)=\frac{2hp}{\kappa^2}
              [p+\kappa(1-h)](\kappa T-L)>0.           \tag{15}
\]
Indeed \(p>h\) and
\(\kappa/({\kappa-1})>3/2\).
On the other slanted piece put \(w=T-u\). The quotient
\(N/w\) decreases affinely in \(w\le L/\kappa\), and
\[
 N(T-L/\kappa,0)=\frac{2hp}{\kappa^2}
              [p+\kappa(h-1)](\kappa T-L)>0.           \tag{16}
\]

Finally \(v=L\) requires
\(L/\kappa\le u\le T-1/2\), since
\(L/\kappa>1/2\) in the present height range.
Concavity in \(u\) reduces this segment to its endpoints.
The left value is (15). For the right value in (14), feasibility
\(T-1/2\ge L/\kappa\) gives
\[
 2p^2-6h^2+4h+1
 \ge4h(1-h+p/\kappa)>0.                               \tag{17}
\]
This proves every boundary piece and hence (13). \(\square\)

## 3. Strict wire-before-leg order, with the original branches

The original wire and inverse leg obey
\[
 X=\frac{q+i}{q-i}=e^{2\pi ix},\qquad
 U=\frac{-i}{2A(q+i)-i},\qquad
 XU=\frac{q+i}{q+i(1+2A/B)}
    =\frac1{1+2iZ},\quad
 Z=\frac{\beta}{\alpha(q+i)}.                          \tag{18}
\]
The rational identity uses \(q^2+1=\alpha+\beta\).
Since
\[
 Z=\frac{q-i}{\alpha}-\frac1{q+i},\qquad
 \Re Z=\frac{N}{(u^2+v^2)D}>0,                         \tag{19}
\]
Lemma 1 proves \(\Im(XU)<0\). All denominators in (18)
are nonzero; in particular \(\Re q>0\) and \(\Re Z>0\)
exclude the displayed possible poles.

**Theorem 2.** On every original positive path charge family with
all powers at least three, every incidence satisfies
\[
                  0<\Re x<\Re s<1/2,
 \qquad s=\frac{i}{2\pi}\Log U.                        \tag{20}
\]
Here the logarithm is the continuous lower-half-plane logarithm
proved in the general inverse-leg theorem.

Indeed the [original wire theorem](research_positive_path_real_wire_order.md)
gives \(0<\Re x\le1/4\), with equality only on an all-complete
edge, and \(X\) has argument in \((0,\pi/2]\).
The inverse leg has \(\arg U\in(-\pi,0)\). Therefore the
sum of these actual arguments lies in \((-\pi,\pi/2)\).
Its sine is negative by (18)--(19), so the sum lies in \((-\pi,0)\).
It is exactly \(2\pi(\Re x-\Re s)\), proving (20).
This argument includes zero-charge vertices and complete edges;
no logarithm is reset.

The theorem supplies the endpoint wire-before-leg inequality and
the regular strip for each difference \(s-x\). It does not prove
\(\Re(s+t)>1/2\) at all vertex/shared pairs, the remaining
type-four source lift condition, or an absolute action identity.
The fixed polynomial certificate is not a numerical root cover.

## 4. Exact reproduction

The checker stores all 50 rational coefficients used in (7), verifies
the displayed algebra and scalar comparisons, and binds the current
analytic inputs. It performs no root proposals or outward sampling.

```sh
python3 experiments/check_mixed_wire_before_inverse_leg.py
python3 experiments/check_mixed_wire_before_inverse_leg.py --input repro/results/research-mixed-wire-before-inverse-leg.json --output repro/results/research-mixed-wire-before-inverse-leg-replay.json
```
