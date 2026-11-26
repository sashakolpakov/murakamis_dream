# The upper transform rows after fixing a complex boundary value

Research deduction, 7 November 2026. The inverse boundary transform
restores terms that vanished at physical boundary indices. This note
bounds every restored row with index at least one half, on the incoming
plateau and its right extension. The outgoing variable is the last
private leg of the original three/four pair. The proof uses the literal
conditional polynomial, not a quotient of the already summed terminal
polynomial.

## 1. The finite sum and the reference

Set
\[
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j.
\]
The part of the conditional polynomial to be estimated is
\[
 C^{\mathrm{up}}_{1,N}(X,Y)
   =\sum_{j=\lceil N/2\rceil}^{N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.                 \tag{1}
\]
It is defined at every nonzero \(X\) and every \(Y\). In particular,
there is no restriction \(j+Nz<N\) when \(Y=e^{-2\pi iz}\) and
\(z\) is not a physical index. The even half row occurs in (1);
at odd levels the first row is just above one half.

Use the original reference of
[the transformed-complement calibration](research_mixed_three_four_transformed_complement_calibration.md):
\[
 a_*=A+ic,\qquad z_*=E+iv,\qquad
 -7/200<c<0,\qquad .349<E<.350,\quad
 -137/4000<v<-1/30.                                      \tag{2}
\]
The first cap is
\[
 U_{0,N}(w,X)=\sum_{j<N}\frac{H_N(w,r^{-j})}{P_j}p_j(X).
\]
The prefix action before the final Gram contraction is
\[
 \mathcal P_{34}(z)=\operatorname{stat}_{a,t}
                         [T_0(a)+Q(t;a,z)],
\quad
 Q(t;a,z)=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat.          \tag{3}
\]
It has its original additive constant. With
\(E_{\rm end}(z)=S(z)-\pi i(z-z^2)/2\), the exact action split is
\[
 M=\Re\mathcal P_{34}(z_*)+\Re E_{\rm end}(z_*),
 \qquad \Re\mathcal P_{34}(z_*)>181/100.                  \tag{4}
\]
These are the established saved-enclosure consequences in the cited
calibration. No root or action is reevaluated here.

## 2. The endpoint comparison holds through incoming angle one half

For \(a=x+ih_a\), \(z=y+ih_z\), define the full absolute row rate
\[
 E_\epsilon(u;a,z)=
 \int_0^u\log|1-e^{-2\pi i(a+s)}|\,ds
 +\int_0^u\log|1-e^{-2\pi i(z+s)}|\,ds
 -(2+\epsilon)J(u)-2\pi h_a u,
 \quad J(u)=\int_0^u\log(2\sin\pi s)\,ds.                \tag{5}
\]
The chirp in (1) contributes the last term. The logarithmic zeros
are integrable and are retained in (5).

**Lemma 1.** If
\[
 x,y\in[11/50,1/2],\qquad |h_a|,|h_z|\le27/250,
 \qquad \epsilon\in\{0,1\},
\]
then
\[
 \max_{1/2\le u\le1}E_\epsilon(u;a,z)
   =\max\{E_\epsilon(1/2;a,z),E_\epsilon(1;a,z)\}.       \tag{6}
\]

*Proof.* The [right-tail endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
proved this assertion with upper angular endpoint \(9/20\).
Here are the angular comparisons needed to extend its proof. All
remaining scalar estimates in that proof concern the fixed corner
\(x=y=11/50\), so their hypotheses do not change.

Write \(x_0=11/50\), \(R_i=e^{-2\pi|h_i|}\), and let
\(G_R'=f_R\), where
\[
 f_R(t)=\log|1-Re^{-2\pi it}|.
\]
The function \(f_R\) is even and increases with \(|t|\) on
\([-1/2,1/2]\). Its primitive can be chosen odd and periodic.
The exact reflection formula of the cited theorem is
\[
 \Phi(v;x,y):=E_0(1-v;x,y)-E_0(1;x,y)
  =-\int_{x-v}^{x}f_{R_1}(t)\,dt
   -\int_{y-v}^{y}f_{R_2}(t)\,dt+2J(v)-\lambda v,
\quad
 \lambda=2\pi\{(-h_a)_++(h_z)_+\}.                      \tag{7}
\]
The following three comparisons hold on the enlarged square.

1. If \(v\le\min(x,y)\), each integration interval is in
   \([0,1/2]\), and its integral is at least \(J(v)\).
   Thus \(\Phi(v;x,y)\le0\). This covers \(v\le x_0\).
2. For \(x_0\le v\le1/2\), the angle-dependent increment
   above the half row is an integral over
   \([x-1/2,x-v]\). Its length is \(1/2-v\), and its center
   is \(x-d\), where \(d=1/4+v/2\). All endpoints stay in
   \([-1/2,1/2]\). Among \(x\in[x_0,1/2]\), the largest
   absolute center is attained at \(x=x_0\), since
   \(2d=1/2+v\ge1/2+x_0\). Therefore
   \[
   \Phi(v;x,y)-\Phi(1/2;x,y)
     \le\Phi(v;x_0,x_0)-\Phi(1/2;x_0,x_0).              \tag{8}
   \]
3. If \(x_0\le v\le2x_0\), the center \(x-v/2\) of the
   interval in (7) is nonnegative. Increasing \(x\) from
   \(x_0\) to \(1/2\) increases its integral, since the
   interval stays in \([-1/2,1/2]\). Hence
   \(\Phi(v;x,y)\le\Phi(v;x_0,x_0)\).

The unrestricted centered-arc upper bound for (7), equation (6) of
the cited endpoint theorem, also has no angular upper restriction.
These are exactly the four angular inputs to its Sections 3--5.
Its corner derivative argument, including the case of a negative
final derivative and its centered envelope, therefore proves (6)
for \(\epsilon=0\) on the enlarged square. Finally,
\(E_1(u)-E_0(u)=-J(u)\le0\) for \(1/2\le u\le1\),
with equality at the two endpoints. This proves the assertion for
\(\epsilon=1\). \(\square\)

## 3. The two endpoint rates at the actual outgoing value

For the rest of the note, take \(a=x+ic\),
\(11/50\le x\le1/2\), and \(z=z_*\).
Both heights are negative. The whole first cap has the supporting
bound from [complete cap support](research_mixed_cap_upper_target_completion.md)
and the normalization in
[the terminal right extension](research_mixed_three_four_private_left_right_extension.md):
\[
 |U_{0,N}(w,e^{-2\pi ia})|
   \le C_\tau N^{B_\tau}e^{N(B_U(x)+\tau)},\qquad
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2,
 \quad p=\Re P_1'(a_*),\quad\kappa_*=1/2500000.        \tag{9}
\]
This holds at complete color and on a sufficiently small fixed
ordinary-color neighborhood after any prescribed positive tolerance.
It is a bound for the complete cap.

The original flattened transform face is pointwise in its private
coordinate. In particular its main private segment contains \(z_*\).
Its phase is
\[
 \Phi(a;t,z_*)=E_{\rm end}(z_*)+Q(t;a,z_*).              \tag{10}
\]
The completed terminal face estimate on \([.22,.45]\), and
Proposition 4 of the cited terminal right extension on \([.45,.5]\),
give
\[
 B_U(x)+\Re\Phi(x+ic;1/2,z_*)\le M-1/20000.            \tag{11}
\]
The private coordinate is not integrated in (11). On the regular
half-row, \(\Re Q(1/2;a,z_*)=E_1(1/2;a,z_*)\).
Subtracting the *constant action* \(\Re E_{\rm end}(z_*)\)
from (11), and using (4), therefore gives
\[
 B_U(x)+E_1(1/2;a,z_*)
       \le\Re\mathcal P_{34}(z_*)-1/20000.             \tag{12}
\]
This does not divide a bound for the summed terminal polynomial.

For the other endpoint, the mean of
\(\log|1-Re^{-2\pi is}|\) over a period is zero when
\(0\le R<1\). This follows directly by integrating its uniformly
convergent power series for \(R<1\). Thus
\[
 E_1(1;a,z_*)=-2\pi c<11/50.                           \tag{13}
\]
For this endpoint use a separate bound for the same complete cap.
The coherent norm estimate in
[the full boundary theorem](research_mixed_three_four_full_boundary_kernel.md),
equation (8), and the centered-arc numerator bound give
\[
 \sup_{w\in[-2,2],\ |X|\le1}|U_{0,N}(w,X)|
   \le C_\tau N^{B_\tau}
             e^{N(433/500+1/3+\tau)}.                 \tag{14}
\]
Indeed use the norm \(\sum_j|H_N(w,r^{-j})/P_j|\) and
\(\max_{j,|X|\le1}|p_j(X)|\), without splitting any coherent
coefficient. The maximum principle gives the disk bound from the
unit-circle bound. Equations (13)--(14) have combined rate less
than \(3/2\), whereas (4) is greater than \(181/100\).

One may use the two cap bounds for the two endpoint terms separately:
if a positive row estimate is at most the sum of its endpoint
exponentials, multiply each summand by the same cap and then apply
its appropriate bound. There is no assertion that one cap ceiling
is always smaller than the other.

## 4. Every restored high row is suppressed

**Theorem 2.** There are a fixed neighborhood \(\mathcal U\) of
\((w,z)=(-2,z_*)\) and constants \(C_{k,\ell}\) such that
\[
 \left|\partial_w^k\partial_z^\ell
 \left[e^{-N\mathcal P_{34}(w,z)}
 U_{0,N}(w,e^{-2\pi i(x+ic)})
 C^{\mathrm{up}}_{1,N}
       (e^{-2\pi i(x+ic)},e^{-2\pi iz})\right]\right|
 \le C_{k,\ell}e^{-N/200000}                            \tag{15}
\]
on a smaller neighborhood, uniformly for \(.22\le x\le.5\),
for every fixed \(k,\ell\) and all sufficiently large integer
\(N\). The phase in (15) is the holomorphic continuation of (3).

*Proof.* At \(z=z_*\), both numerator radii are strictly less
than one and remain so on a fixed neighborhood. Uniform Riemann
sum bounds for their smooth logarithms give the two numerator
integrals in (5), with error \(O(1)\). For the denominator,
\[
 \log|P_j|=NJ(j/N)+O(\log N)\qquad(0\le j<N)           \tag{16}
\]
uniformly in \(j\). To see the endpoint uniformity, subtract
\(\log t+\log(1-t)\) from \(\log(2\sin\pi t)\).
The difference extends smoothly to the closed unit interval; its
Riemann sum has bounded error. The two remaining logarithmic sums
are compared with their integrals by monotonicity, with error
\(O(\log N)\). No numerator zero is discarded in this argument.

Consequently the absolute sum of the rows in (1) is bounded by
a polynomial in \(N\) times
\[
 e^{NE_1(1/2;a,z_*)}+e^{NE_1(1;a,z_*)},                 \tag{17}
\]
by Lemma 1. Apply (9),(12) to the first term and (13),(14) to
the second. This leaves a raw gap at least \(1/20000\) below
\(\Re\mathcal P_{34}(z_*)\), before arbitrarily small cap
tolerances and polynomial factors are paid.

The numerator logarithms vary uniformly continuously with \(z\)
on this compact negative-height domain. Thus the same row bounds,
with any specified additional tolerance, hold on a small fixed
neighborhood of \(z_*\). The cap estimate (9) has the analogous
ordinary-color continuation. For (14) it also follows directly
from the polynomial Bernstein bound: a degree at most \(N-1\)
polynomial with a real-interval bound incurs arbitrarily small
exponential cost on a sufficiently small fixed neighborhood of
\(-2\). The calibrated action in (3) is holomorphic and continuous
there by the nonsingular original Hessian.

Choose these neighborhoods and tolerances to spend less than half
the raw gap. After absorbing polynomial factors, the normalized
holomorphic function has a uniform exponential gap larger than
\(1/200000\). Cauchy's formula on smaller fixed neighborhoods
gives all the derivatives in (15), with this same weakened gap.
The actual index set (1) retains both parity cases. \(\square\)

Multiplication by the external factor \(N\), and integration over
this fixed incoming interval, preserve an exponential gap after a
further harmless weakening. This settles the restored upper rows
on the plateau and right extension. It leaves the lower rows and
their contour deformation, the incoming left taper, and propagation
to the boundary values selected by longer words to be proved
separately. It is not a whole-prefix asymptotic.
