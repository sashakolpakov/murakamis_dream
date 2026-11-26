# A free outside neighborhood for the actual pair-edge kernel

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The complete-end logarithmic estimate can be strengthened to the full
Gaussian edge packet, with a fixed small complex neighborhood in the
outside color. The proof below uses the original finite Newton sum.
Its contour is a ray in the tangent coordinate, rather than a horizontal
line. All low-index endpoints, reciprocal-factorial terms, cotangent
aliases, and the original radical are retained.

## 1. Domain and statement

Write \(t=a-iH\), and put
\[
 C=\cos(t/2),\qquad A=C^2,\qquad
 \mathcal D=\{\,0<a<\pi/2,\ H>0,\ |C|<1\,\}.
 \tag{1}
\]
On this domain \(C\) is in the first quadrant,
\(\Re A>1/2\), and \(0<\arg C<\pi/4\).
Fix a compact subset \(\mathcal T\) of
\(\mathcal D\cap\{H<107/100\}\).
Every active angle of a fixed positive integer complete-end internal
pair belongs to this domain, by the
[real wire-order theorem](research_positive_path_real_wire_order.md)
and the [pair complete-edge gap](research_internal_pair_complete_edge_gap.md).

Use the original conventions
\[
 \begin{split}
 K_N(t,u)&=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),\\
 L_N(t,u)&=\sum_{j=0}^{N-1-\lfloor N/2\rfloor}
                         e_j(-2\cos t)e_j(-2\cos u),\\
 b(y,t)&=-J(1/2-y+t/(2\pi))-J(1/2-y-t/(2\pi))-2J(y),\\
 F(y;t,u)&=b(y,t)+b(y,u),\qquad J'(y)=\Log(2\sin\pi y).
 \end{split}
 \tag{2}
\]
The branches are continued from completeness without resetting a
logarithm after crossing a factorial strip.

**Theorem 1.** There are a complex neighborhood \(V\) of \(\mathcal T\)
and \(\epsilon>0\) such that, uniformly for \(t\in V\), \(|u|<\epsilon\),
through both level parities,
\[
 \begin{split}
 K_N(t,u)&=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                                      (1+O(N^{-1})),\\
 a_e(t,u)&=\frac{\sqrt{2\pi}}
 {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}\ne0 .
 \end{split}
 \tag{3}
\]
Here \(y_*\) is the selected wire saddle and
\(\psi(t,u)=F(y_*;t,u)\) has the original complete constant.
The Gaussian root is continued from positive real \(C\).
The normalized error has a holomorphic expansion to every fixed
inverse-power order, with all fixed parameter derivatives on smaller
neighborhoods. Evenness in \(u\) gives the same assertion in a fixed
ordinary outside-color neighborhood of \(-2\), including its normals.
The same packet holds for \(L_N\), and \(K_N/L_N=1+O(e^{-cN})\).

The theorem concerns an actual edge factor near the selected pair
angles. It does not determine the coefficient of a joint trace cycle.

## 2. A strict single-maximum contour at the complete outside end

Set \(u=0\) and \(z=\tan(\pi y)\). Direct differentiation of (2) gives
\[
 e^{F_y}=\frac{A-(1-A)z^2}{z^4}.
 \tag{4}
\]
Thus the finite critical equation factors as
\((z^2-A)(z^2+1)=0\). The selected saddle is
\(z=C\), or \(y_*=\pi^{-1}\arctan C\).

Consider the oriented ray
\[
 z=Cr,\quad 0<r<\infty,\qquad
 y=\pi^{-1}\arctan(Cr).
 \tag{5}
\]
It is the graph \(y=x+ih(x)\), \(0<x<1/2\), where
\[
 h(x)=\frac1{2\pi}
       \operatorname{arsinh}\{\tan(\gamma)\sin(2\pi x)\},
                  \qquad \gamma=\arg C.
 \tag{6}
\]
Its endpoints are \(0\) and \(1/2\).

**Lemma 2.** Along (5), \(\Re F\) strictly increases to \(r=1\)
and strictly decreases thereafter. At the maximum,
\[
 F_r(1)=0,\qquad F_{rr}(1)=-\frac2{\pi C},
 \qquad F_{yy}(y_*)=-\frac{2\pi(1+A)^2}{C^3}.
 \tag{7}
\]

*Proof.* On the ray let
\[
 R(r)=\frac{1-(1-A)r^2}{Ar^4},\qquad
 F_r=\frac{C}{\pi(1+Ar^2)}\Log R(r).
 \tag{8}
\]
For \(r<1\),
\(R=r^{-4}\{r^2+(1-r^2)/A\}\) has negative argument and
\(|R|>1\): its real part exceeds \(r^{-2}>1\).
The tangent in (8) has positive real and imaginary parts because
\(|A|r^2<1\). Hence \(\Re F_r>0\).

For \(r>1\), \(R\) is in the upper half-plane and \(|R|<1\).
Indeed, writing \(v=r^2>1\), the difference of squared moduli
is
\[
 |A|^2v^4-|1-(1-A)v|^2
 =(v-1)\{|A|^2(v^3+v^2)+(2\Re A-1)v+1\}>0.
 \tag{9}
\]
Until \(r=|A|^{-1/2}\) the tangent has nonnegative imaginary
part, so \(\Re F_r<0\).

For the remaining interval put \(v=r^{-2}\le s=|A|<1\).
Now
\[
 R=v(A-1+v)/A,\qquad
 \frac{|\Im(C/(v+A))|}{\Re(C/(v+A))}
                  =\tan\gamma\,\frac{s-v}{s+v}.
 \tag{10}
\]
Because \(2\Re A\ge1\), \(|A-1+v|\le|A|\); consequently
\[
 -\log|R|\ge-\log v\ge\frac{2(1-v)}{1+v},\qquad
 0<\arg R<\pi-2\gamma .
 \tag{11}
\]
Also \((s-v)/(s+v)\le(1-v)/(1+v)\) and
\(\tan\gamma(\pi-2\gamma)<2\) for \(0<\gamma<\pi/4\).
For the latter inequality the expression is increasing on this
interval, since \(\pi-2\gamma>\sin(2\gamma)\), and its endpoint
value is \(\pi/2<2\).
Equations (10)--(11) therefore show that the negative real-log
term in (8) strictly exceeds its possible positive argument term.
This proves \(\Re F_r<0\).
The logarithm tends to zero at \(r=1\) from both sides.
Differentiation there proves (7), including the zero logarithmic
lift. \(\square\)

The only possible numerator zero in the upper wire strip is
\[
 y_0=\frac12-\frac{t}{2\pi},\qquad
 \tan(\pi y_0)=\cot(t/2)=C/\sin(t/2).
 \tag{12}
\]
Since \(\sin(t/2)\) is in the fourth quadrant, its tangent
coordinate has argument strictly greater than \(\gamma\).
Thus \(y_0\) lies above the graph (6). In particular neither the
ray nor the closed region between it and its reflection meets
this zero. All continuations used in (8) are regular there.
At the endpoints the continued phase has
\[
                    F(0;t,0)=0,\qquad F(1/2;t,0)=it/2 .
 \tag{13}
\]
The second equality uses
\(J_+(-t/(2\pi))=-J(t/(2\pi))-it/2\).
The real endpoint rates are therefore \(0\) and \(H/2\).
The complete-edge gap gives
\(\Re\psi(t,0)>H+1/500\), uniformly on \(\mathcal T\).

## 3. The reflected contour controls the lower lattice alias

For fixed \(x\in(0,1/2)\) and \(0\le v\le h(x)\), define
\[
 D_x(v)=\Re F(x-iv;t,0)-\Re F(x+iv;t,0).
 \tag{14}
\]
The complete factor \(b(y,0)\) cancels in this difference.

**Lemma 3.** One has \(D_x(v)<2\pi v\) for \(v>0\).

*Proof.* Write \(\cos t=c+id\), where \(c,d>0\), and put
\[
 R_v=\cos(2\pi x)\cosh(2\pi v)+c,\qquad
 B_v=\sin(2\pi x)\sinh(2\pi v).
 \tag{15}
\]
Differentiating (14), the sine-denominator arguments cancel and
give
\[
 D_x'(v)=\arg\{R_v+i(d+B_v)\}
              +\arg\{R_v+i(d-B_v)\}.
 \tag{16}
\]
Both arguments start in \((0,\pi)\) and are continued from
\(v=0\). There is no zero in the range under consideration
by (12). The first argument always belongs to \((0,\pi)\).
If the second remains at most \(\pi\), their sum is less than
\(2\pi\). Otherwise \(R_v<0\), \(B_v>d\), and its continued
argument is
\(\pi+\arctan((B_v-d)/(-R_v))\). The first argument is then
\(\pi-\arctan((B_v+d)/(-R_v))\), so their sum is again strictly
less than \(2\pi\).
There is no additional winding: for \(x\le1/4\) the real part
\(R_v\) is positive; for \(x>1/4\) both the real and imaginary
parts of \(R_v+i(d-B_v)\) decrease with \(v\).
Since \(D_x(0)=0\), integration proves the claim. \(\square\)

Consequently the lower reflected ray, after its exact cotangent
penalty, satisfies
\[
 \Re F(x-ih(x);t,0)-2\pi h(x)
                         <\Re F(x+ih(x);t,0)\le\Re\psi(t,0).
 \tag{17}
\]
The upper nonconstant cotangent term has the additional penalty
\(2\pi h(x)>0\). These strict inequalities give uniform gaps on
every compact subarc, uniformly for \(t\in\mathcal T\).

## 4. The original finite contour and both endpoint sectors

Choose fixed \(0<\alpha<\beta<1/2\), sufficiently close to \(0\)
and \(1/2\), respectively. By (13), continuity, and compactness,
the two short endpoint arcs, the two vertical connectors between
the ray and its reflection at these cuts, and the omitted real
intervals all have rate strictly below \(\Re\psi(t,0)\).
The cuts contain the selected saddle for every \(t\in\mathcal T\).
Move them by \(O(N^{-1})\) to half-grid lines; all strict gaps
persist.

Use the exact factorial interpolation
\[
 B_N(y,t)=\frac{N}
 {G_N(N(1/2-y+t/(2\pi))-1/2)
  G_N(N(1/2-y-t/(2\pi))-1/2)G_N(Ny)^2}.
 \tag{18}
\]
This sampling equality is an ordinary entire identity in \(t\),
not merely equality of physical jets. Indeed the
[exact factorial reflection identity](exact_factorial_interpolation_and_complex_contours.md)
\(G_N(z)G_N(N-1-z)=N\) holds identically. Applying the integer
shift identity to the two factors in this product gives
\[
 B_N(j/N,t)=S_j^{-2}\prod_{\ell=0}^{j-1}
          \{2\cos((2\ell+1)\pi/N)+2\cos t\}
                         =e_j(-2\cos t).
\]
In particular \(B_N(0,t)=1\) exactly, for arbitrary complex \(t\).
The defining Gamma product makes (18) holomorphic on the region
between these two truncated rays: the reciprocal-factorial zeros
at negative integer arguments create no poles, and the first
positive factorial zeros lie outside the region.

The [uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md)
apply on the entire contour. When
\(\Re(1/2-y-t/(2\pi))<0\), its imaginary part is positive
throughout this region, by (12). Use the upper continuation and
the exact identity
\[
 \frac1{G_N(Nw-1/2)}
   =\frac{e^{-i\pi Nw}}N(1+e^{2\pi iNw})G_N(-Nw-1/2).
 \tag{19}
\]
Both terms are included. Their sum is bounded by the continued
phase in (2); no value is assigned by discarding a Newton zero.
Near the saddle all factorial real parts are positive.
The usual full factorial expansion there is
\[
 B_N(y,t)B_N(y,0)=
       \frac{e^{NF(y;t,0)}}{4N^2\sin^2(\pi y)}
                                  (1+O(N^{-1})).
 \tag{20}
\]
For any prescribed further order, apply the sectorial Stirling
formula through that order to each Gamma factor in the defining
product. On this compact saddle neighborhood the arguments
\(Nw\) and \(N(k\pm w)\) stay in fixed sectors away from the
negative real axis and zero. The remainder after the
\(N^{-(2q-1)}\) term is bounded by
\(C_qN^{-(2q+1)}k^{-(2q+1)}\) for the \(k\)-th product factor.
It is summable, while the finitely many initial factors have
the same uniform sectorial bound. This extends (20) to every
fixed order. Only the exact upper bounds, not this relative
expansion, are used on the remaining contour and its reflected
factorial faces.

Enclose exactly the retained integers by
\(\pi N\cot(\pi Ny)\). On the upper and lower rays this equals
\(\mp i\pi N+O(N e^{-2\pi N|\Im y|})\).
Equations (17) and (13) bound every nonconstant term and every
vertical current below the selected rate. The two constant
horizontal terms combine to \(+N\) times the oriented principal
wire integral; Cauchy deformation between the rays introduces
only the already bounded endpoint connectors.
Lemma 2 supplies its unique strict maximum and nonzero Gaussian
coefficient. Thus the actual retained sum has (3).

For completeness the omitted original low indices satisfy,
uniformly up to both endpoints,
\[
 |e_j(-2\cos t)e_j(-2)|
       \le N^C\exp\{N\Re F(j/N;t,0)\}.
 \tag{21}
\]
This follows directly from the same midpoint factorial bounds,
now keeping \(G_N(Nj/N)\) exact at \(j=0\).
Replacing \(J(x+1/(2N))\) by \(J(x)\) costs \(O(\log N)\)
in the exponent uniformly for \(0\le x\le1/2\).
The zero or half-integer final factorial argument is covered by
the midpoint estimate. Hence (21) covers both possible final low
indices, and the endpoint gaps prove the omitted finite sums
are exponentially smaller.

## 5. A fixed complex outside neighborhood and the full kernel

All contour and tail inequalities just proved are strict on
compact sets. The real upper exponent of the exact reciprocal
factorial is continuous across zero and across either side of
the negative real axis. Therefore the same bounds persist
uniformly for \(t\) in a slightly larger complex neighborhood
and \(|u|<\epsilon\), after decreasing \(\epsilon>0\).
For the real omitted indices this uses the continuous factorial
upper exponent, not an analytic continuation of their errors
from \(u=0\).

On the retained contour the outside factorial arguments have
positive real part if \(\epsilon\) is small enough.
The selected saddle moves holomorphically. Locally deform the
principal ray through this saddle; outside a fixed small saddle
neighborhood all gaps persist, and inside it the nonzero
quadratic derivative (7) gives the ordinary holomorphic Gaussian
expansion. This proves (3) for \(L_N(t,u)\), uniformly with every
fixed inverse-power order. The exact contour and normalized
errors are holomorphic, so Cauchy estimates retain fixed
derivatives on smaller neighborhoods.

Finally the
[original radical Fourier estimate](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials)
and its polynomial degree give
\[
 |K_N(t,u)-L_N(t,u)|
          \le N^2 e^{(N-1)(|\Im t|+|\Im u|)}.
 \tag{22}
\]
By the complete-edge gap and continuity,
\(\Re\psi(t,u)>|\Im t|+|\Im u|+c\) on a sufficiently
small fixed neighborhood, for some \(c>0\).
Thus (22) is exponentially small relative to the packet, with
all fixed derivatives after shrinking the neighborhoods.
This establishes Theorem 1 for the full original kernel.
In particular the extension preserves the outside ordinary
normal: even holomorphy in \(u\) descends through
\(-2\cos u=-2+u^2+O(u^4)\).

No joint-cycle lower bound is asserted. The conclusion supplies
an independently normalized free-boundary edge factor for a
subsequent original trace or Fourier contraction.

For a fixed integer pair, the selected charge-cube image is compact.
Its nonzero angles satisfy (1), while its zero angles have neighborhoods
covered by the [thin-rectangle kernel theorem](research_bare_kernel_thin_rectangle.md).
A finite cover therefore supplies one common outside neighborhood
for this fixed pair's entire charge cube. This conclusion still
concerns the individual edge kernel.

## 6. Independent finite normalization record

The [focused checker](../experiments/check_pair_free_boundary_kernel.py)
verifies (9) and the derivative identities symbolically. It compares
the finite Barnes-product factorial interpolation with original Newton
products and ordinary normals at genuinely complex selected and
outside angles, through both parities. Its separate comparisons of
the full and low finite sums with (3) are normalization diagnostics,
not the proof of a uniform asymptotic.
The [saved record](../repro/results/research-pair-free-boundary-kernel.json)
includes the script, direct dependency, and proof hashes.

## 7. Whole outside-period decay and a complex strip

The same actual contours give a bound useful before a subsequent
trace or Fourier contraction. This requires a global factorial
estimate, not merely positivity of the finite physical samples.

**Theorem 4.** After shrinking \(V\) around \(\mathcal T\), there
are constants \(c,B,h_0>0\) and \(C,A_0<\infty\) such that
\[
 |K_N(t,u+iv)|\le C N^{A_0}
 \exp N\{\Re\psi(t,0)-c(1-\cos u)+Bv^2\},
 \quad -\pi\le u\le\pi,\quad |v|\le h_0,\quad t\in V .
 \tag{23}
\]
All fixed selected-variable and outside-angle derivatives obey
the same bound after increasing the polynomial power and
shrinking the parameter neighborhoods. This includes fixed
ordinary outside-color normals at the complete point and
throughout the real color interval.

*Proof of the real-period bound.* Keep the finite cuts and the
upper and lower contours of Section 4. Every retained contour
point satisfies
\(\alpha/2<\Re y<(1/2+\beta)/2<1/2\) and a uniform height bound.
The exact
[factorial boundary inequality](research_uniform_factorial_and_boundary_decay.md#4-decay-in-the-real-boundary-angle)
therefore gives a common \(c_1>0\) with
\[
 |B_N(y,u)|\le \frac{C}{N}
       \exp N\{\Re b(y,0)-c_1(1-\cos u)\},
                      \qquad -\pi\le u\le\pi .
 \tag{24}
\]
This inequality holds on both rays and on every connector.
For all these real \(u\), the shifted factorial real parts
stay in a fixed subinterval of \((-1,1)\). If a shifted
argument is negative, its exact reciprocal reflection retains
both exponential terms, as in (19). The real upper exponent
uses the side approached by that argument; its boundary
values agree at the negative real axis. Thus (24) remains
valid at its zeros and on its reflected sectors.

Multiply (24) by the old bound for \(B_N(y,t)\).
Every principal contour integral, every cotangent alias and
every vertical current from Section 4 keeps its old exponent,
with the additional loss \(c_1(1-\cos u)\).
In particular this argument bounds the principal integral
even when its saddle moves far from the complete one.

For the omitted original low indices, the exact positive
Fourier expansion of the
[low Newton polynomials](research_zero_power_internal_boundary_theorem.md#2-positive-laurent-coefficients-and-angular-decrease)
implies
\[
 |e_j(-2\cos u)|\le e_j(-2),\qquad 2j<N,\quad u\in\mathbb R.
 \tag{25}
\]
The condition includes the final low index at both parities.
Their old finite-tail gap therefore remains valid throughout
the real outside period. The radical bound (22) likewise
has its old strict gap when \(u\) is real. If \(\delta>0\)
is the smaller of these gaps, choose
\(c_2\le\min(c_1,\delta/4)\). Since \(1-\cos u\le2\),
these two error sectors also satisfy
\[
 |K_N(t,u)|\le C N^{A_0}
       e^{N\{\Re\psi(t,0)-c_2(1-\cos u)\}} .
 \tag{26}
\]
This proves the real-period assertion with the original
factorial currents and the full radical included.

*Proof of the strip bound.* Near \(u=0\), Theorem 1 and the
original phase derivative give
\[
 \psi(t,z)-\psi(t,0)=-\frac{\cos(t/2)}{4\pi}z^2+O(z^4).
 \tag{27}
\]
The real part of \(\cos(t/2)\) is bounded below by a positive
constant on the chosen compact \(t\)-domain. Young's inequality
for the mixed \(uv\) term in (27), followed by decreasing the
neighborhood, gives
\[
 \Re\{\psi(t,u+iv)-\psi(t,0)\}
                    \le-\kappa u^2+B_0v^2
 \tag{28}
\]
for some \(\kappa>0\). The nonzero bounded amplitude and
relative error in (3) prove (23) on this local neighborhood.

For the complementary real angles use the actual finite
Laurent degree. Put
\(f_N(z)=e^{-N\psi(t,0)}K_N(t,z)\), of angular degree at most
\(D=N-1\). The function \(Z^D f_N(z)\), \(Z=e^{iz}\), is a
polynomial in \(Z\). The subharmonic Poisson bound in the disk,
applied to (26), and the analogous reciprocal polynomial for
the other half-plane give
\[
 \log|f_N(u+iv)|\le
 \log(CN^{A_0})+D|v|
       -c_2N\{1-e^{-|v|}\cos u\}
 \le\log(CN^{A_0})+
       N\{-c_2(1-\cos u)+(1+c_2)|v|\}.
 \tag{29}
\]
Equivalently, apply the maximum principle to the polynomial
\(Z^Df_N(z)\) multiplied by \(e^{-c_2NZ}\): its boundary
modulus is at most \(CN^{A_0}e^{-c_2N}\).
This proves (29) directly even in the presence of zeros.
Outside a fixed smaller interval
about zero, \(1-\cos u\) has a positive lower bound.
Choose \(h_0>0\) small enough that the last linear cost in
(29) is absorbed by half of this angular loss.
Combining with (28) proves (23), for
\(c\le\min(c_2/2,2\kappa)\) and \(B\ge B_0\).
This step uses the finite polynomial on the whole circle,
not an analytic continuation of a pointwise asymptotic.

Finally, apply Cauchy's formula to the holomorphic normalized
function \(e^{-N\psi(t,0)}K_N(t,z)\).
Fixed \(t\)-derivatives may use fixed smaller neighborhoods;
angle derivatives use circles of radius \(1/N\), on which
the exponent in (23) changes by \(O(1)\).
Thus only polynomial factors in \(N\) are lost.
For ordinary outside-color derivatives use color circles
of radius \(O(N^{-2})\): the inverse cosine changes by
\(O(N^{-1})\) uniformly on this compact strip, including
its two quadratic branch points. The even finite polynomial
is single-valued in the color there. Cauchy's formula again
costs only powers of \(N\).
The selected ordinary normal follows on \(V\) from
\(\sin t\ne0\), or from the thin theorem in a neighborhood
of a zero charge. \(\square\)

The constants in (23) can likewise be made common over the
fixed pair's charge cube by the finite cover already described.
On its thin neighborhoods of zero charge, apply (24) to the
existing thin theorem's finite wire contours; their endpoint
and alias gaps, the same low-index positivity, and their
radical gap give (26). The local thin packet and (29) then
give the identical strip argument there.
This supplies the edge estimate and its exact observation
normals needed in a composition argument. It does not provide
the missing joint trace-cycle coefficient.
Evenness and the real coefficients of the original Newton
polynomials give the conjugate statements at mirrored selected
angles, with the conjugated phase and the same absolute bounds.
