# The complete complementary contour of the ordinary three/four source

Research assembly, 7 November 2026. The saved original-action enclosure
supplies enough room to bound the complete complementary contour by
the original finite transform rows. All private endpoint coefficients
remain coherent. A short vertical connector is followed by the real
far half-circle; both pieces have a strict calibrated source gap.
Together with the completed first half this proves the nonzero
whole ordinary three/four asymptotic at complete boundary colors.
No new numerical evaluation is used.

## 1. Original source and the two saved scalar consequences

Retain the exact functions of
[the ordinary pair source](research_mixed_three_four_ordinary_pair_target.md):
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
            \frac{H_N(w,r^{-j})p_j(X)}{P_j},\\
 V_{1,N}(w,X)&=\sum_{i=0}^{N-1}
          \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i),\\
 Z_{34,N}(w_L,w_R)&=\kappa_N^3N^2\int_0^1
 U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})\,da.
\end{split}                                                     \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(|\kappa_N|=1\).
The complete-color geometric reference is \(a_*=A+ic\),
with its original action and symbols
\[
 \mathcal S=T_0(a_*)+P_1(a_*),\quad M=\Re\mathcal S,
 \quad H=-(T_0+P_1)''(a_*),\quad
 \mathcal A=\frac{\sqrt{2\pi}\,b_U(a_*)b_V(a_*)}{\sqrt H}\ne0.
                                                               \tag{2}
\]
These are the same quantities and Gaussian branch as in
[the first-half assembly](research_mixed_three_four_first_half_assembly.md).

The sole approved diagnostic is the saved file
[research-mixed-three-four-half-face-witnesses-attempt01.json](../repro/results/research-mixed-three-four-half-face-witnesses-attempt01.json),
SHA256
`fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70`.
Its original six-variable Krawczyk enclosure and action identification,
under the frozen [protocol](research_mixed_three_four_half_face_witness_protocol.md),
give the two consequences used here:
\[
                         M>27/10,\qquad -7/200<c<0.
                                                               \tag{3}
\]
The stored original-action lower enclosure starts with
\(2.7049005864\), while the attached-coordinate imaginary interval
lies in \((-.033943377,-.033943374)\). The inequalities (3)
are coarse consequences of those stored bounds, not new evaluations.
The diagnostic's six separate witness comparisons remain
inconclusive. Their signs are neither changed nor used in this proof.

## 2. A full finite row bound, with no private contour remaining

Put
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du\quad(0\le t\le1),
 \qquad L(t)=-2J((1-t)/2),\quad b_1=433/500.
                                                               \tag{4}
\]
Use the continuous periodic extension of \(J\) when an argument
leaves this interval. The source estimate in
[the physical far-half theorem](research_mixed_three_four_physical_far_half.md),
equations (15)--(18), is uniform over **every** physical transform
index \(i<N\):
\[
 |U_{1,N}(w,r^i)|
 \le C_\tau N^{B_\tau}
           e^{N\{b_1+L(t)-J(t)+\tau\}},\qquad t=i/N.
                                                               \tag{5}
\]
Its exact source is
\[
 U_{1,N}(w,r^i)=\sum_{j=0}^{N-1-i}
       \frac{H_N(w,r^{-j})}{P_j}
                       \frac{P_{i+j}}{P_iP_j}.
                                                               \tag{6}
\]
The quotient rate has maximum \(L(t)-J(t)\) on its full
physical support. The remaining sum of complete \(H_N/P_j\)
moduli has the original coherent ceiling \(b_1\).
Thus (5) retains the whole private and Newton sum, both true
transform ends and both parities. No compact packet is extrapolated
to an endpoint, and no physical incoming termination is imposed.

For \(a=x+ih\), let
\[
 I_{x,h}(t)=\int_0^t
                \log|1-e^{2\pi h}e^{-2\pi i(x+u)}|\,du.
                                                               \tag{7}
\]
The original positive-row rate in \(V_1\), including its
\(X^{-i}\) chirp, is therefore
\[
                 b_1+L(t)-3J(t)+I_{x,h}(t)-2\pi ht.
                                                               \tag{8}
\]
The zero-safe numerator upper estimate is uniform on every compact
\((x,h,t)\) domain. The nonzero denominator factorials have
their uniform \(O(\log N)\) error. These facts are proved by
the truncated-log argument in
[the global transform-end theorem](research_mixed_three_four_global_transform_ends.md),
Section 3. They include a numerator zero and the indices \(i=0,N-1\).

The first factor is whole throughout. The
[radial far-half theorem](research_mixed_three_four_far_half_cap_radial_extension.md)
gives its ceiling
\[
 |U_{0,N}(w,e^{-2\pi i(x+ih)})|
 \le C_\tau N^{B_\tau}e^{N\{B_0+\tau\}},\qquad
 B_0=1549/1500,\quad 1/2\le x\le1,\quad c\le h\le0.
                                                               \tag{9}
\]
Its proof keeps all private rows, including those that revive
between physical incoming roots.

## 3. The original real far half is paid

For \(h=0\), the exact integral comparison in
[the continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md),
Lemma 1, is
\[
 I_{x,0}(t)\le
 \begin{cases}
    -J(1/2-t),&0\le t\le1/2,\\
    J(t),&1/2\le t\le1,
 \end{cases}\qquad 1/2\le x\le1.
                                                               \tag{10}
\]
Set
\[
                    D(t)=L(t)-J(1/2-t)-3J(t).
                                                               \tag{11}
\]
The written quadratic support in
[the half-face scalar theorem](research_mixed_three_four_physical_half_face_ceiling.md),
equations (14)--(17), proves directly
\[
 \max_{0\le t\le1/2}D(t)
 <\frac7{40}-\frac3{512}+\frac{73}{125}+\frac1{2000}
 <\frac{377}{500}.
                                                               \tag{12}
\]
The second inequality is \(3/512>11/2000\).
For clarity, (12) is a bound for the scalar \(D\) itself;
it is not inferred by reversing an upper bound for a larger envelope.
Its proof uses
\(D''\le-2\pi\sqrt3\), the tangent at \(t=1/4\), and
the already proved bound \(-4J(1/4)<73/125\).

Equations (8)--(12) bound all \(t\le1/2\) by the total rate
\[
              B_0+b_1+377/500=3979/1500,
 \qquad 27/10-3979/1500=71/1500.
                                                               \tag{13}
\]
For \(t\ge1/2\), the elementary maximum in
[the continuous upper-row theorem](research_mixed_three_four_continuous_far_half_upper_rows.md),
Lemma 1, gives
\[
 L(t)-2J(t)\le-2J(1/4)<73/250.
                                                               \tag{14}
\]
These rows have total rate less than
\(B_0+b_1+73/250=1643/750\), also strictly below (3).
Thus every transform row of the continuous real far half is included.

## 4. The entire vertical connector is paid

Take \(a=1/2+ih\), \(c\le h\le0\), and put
\[
                  \delta=-2\pi h,\qquad R=e^{-\delta}.
\]
From (3) and \(\pi<22/7\),
\[
                       0\le\delta<11/50.
                                                               \tag{15}
\]
For \(0\le t<1/2\), the exact modulus identity gives
\[
\begin{split}
 I_{1/2,h}(t)-I_{1/2,0}(t)
   &=-\frac{\delta t}{2}
     +\frac12\int_0^t
       \log\left(1+\frac{\cosh\delta-1}{2\cos^2\pi u}\right)du.
\end{split}                                                     \tag{16}
\]
Including the original \(+\delta t\) chirp cost, define
\[
 D_\delta(t)=L(t)-3J(t)+I_{1/2,h}(t)+\delta t.
                                                               \tag{17}
\]
For \(t\le1/3\), equations (16)--(17) and
\(\log(1+z)\le z\) give
\[
 D_\delta(t)-D(t)
 \le\frac{\delta t}{2}
        +\frac{\cosh\delta-1}{4\pi}\tan\pi t
 <\frac{11}{300}+\frac7{1920}.
                                                               \tag{18}
\]
Here \(\tan\pi t\le\sqrt3<7/4\), \(\pi>3\), and
\(\cosh\delta-1<1/40\). The last bound has the exact
elementary witness
\[
 \cosh\delta-1
 \le\frac{\delta^2}{2(1-\delta^2/12)}
 <\frac{726}{29879}<\frac1{40}.
                                                               \tag{19}
\]
The series estimate uses that every ratio after the first
nonconstant term is at most \(\delta^2/12\).

The restriction \(t\le1/3\) in (18) does not discard the
remaining lower-half transform rows. Direct differentiation gives
\[
 \exp D_\delta'(t)
   =\frac{2\cos(\pi t/2)
          |e^\delta+e^{-2\pi it}|}{(2\sin\pi t)^3}.
                                                               \tag{20}
\]
For \(1/3\le t<1/2\), the first numerator is at most
\(\sqrt3\) and the denominator is at least \(3\sqrt3\).
Also \(1\le e^\delta<5/4\). A rational witness is
\[
 e^{11/50}
 \le1+\frac{11}{50}
       +\frac{(11/50)^2}{2(1-11/150)}
   =\frac{17321}{13900}<\frac54.
                                                               \tag{21}
\]
Since \(\cos2\pi t\le-1/2\),
\[
 |e^\delta+e^{-2\pi it}|^2
   \le e^{2\delta}-e^\delta+1
   <21/16<(6/5)^2.
                                                               \tag{22}
\]
Thus \(\exp D_\delta'(t)<2/5\). The function strictly
decreases on this interval, and its continuous endpoint at \(1/2\)
is included. Combining (12), (18), and (20)--(22) bounds all
\(0\le t\le1/2\) by the total rate
\[
 B_0+b_1+D_\delta(t)
 <\frac{3979}{1500}+\frac{11}{300}+\frac7{1920}
 =\frac{27}{10}-\frac{337}{48000}
 < M-\frac1{150}.
                                                               \tag{23}
\]
The equality follows from
\(71/1500-11/300-7/1920=337/48000\), and
\(337/48000>1/150\).

For \(1/2\le t\le1\), a simpler estimate suffices. At
\(0<R\le1\), the half-period integral of
\(f_R(u)=\log|1-Re^{-2\pi iu}|\) is zero. Consequently
\[
 I_{1/2,h}(t)=\int_0^{t-1/2}f_R(u)\,du\le0.
                                                               \tag{24}
\]
Indeed \(f_R\) increases on \([0,1/2]\), so its integral
as a function of its upper endpoint is convex, with values zero
at both endpoints. The statement at \(R=1\) follows by
continuity of the integrable logarithm.
Since \(J(t)\ge0\), \(L(t)<1/3\), and \(\delta t<11/50\),
these rows have total rate less than
\[
 B_0+b_1+1/3+11/50=613/250<27/10-1/150.
                                                               \tag{25}
\]
Thus the entire vertical connector, not only a central transform
interval, has been bounded.

## 5. Finite-source conclusion and the original full contour

Let \(\Gamma_+\) first run upward from \(1/2+ic\) to
\(1/2\), then along the real interval from \(1/2\) to one.
All estimates above concern the literal source (1) on this path.
The uniform product estimates, coefficient bounds and row count
contribute one arbitrarily small total exponential tolerance and a
polynomial prefactor. Choose the total tolerance below \(1/300\).
The strict reserve (23) then proves:

**Theorem 1.** On sufficiently small fixed ordinary-color disks,
for every fixed pair of ordinary derivative orders,
\[
 \begin{split}
 &|\partial_{w_L}^{k}U_{0,N}(w_L,X)|\\
 &\quad\cdot\sum_{i=0}^{N-1}
    \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
              |\partial_{w_R}^{\ell}U_{1,N}(w_R,r^i)|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{N(M-1/300)}
            \qquad(a\in\Gamma_+,\ X=e^{-2\pi ia}).
 \end{split}                                                    \tag{26}
\]
Every true row, physical zero, complete private coefficient, and
both level parities are retained. Fixed ordinary derivatives follow
from the uniform complete-coefficient bounds on slightly larger
color disks, or rowwise Cauchy estimates before summing.

To avoid ambiguity in the contour statement, its consequence is
\[
 \left|\partial_{w_L}^k\partial_{w_R}^{\ell}
  \left[\kappa_N^3N^2\int_{\Gamma_+}U_{0,N}(w_L,e^{-2\pi ia})
                       V_{1,N}(w_R,e^{-2\pi ia})\,da\right]\right|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{N(M-1/300)}.
                                                               \tag{27}
\]
The length of \(\Gamma_+\) is bounded, and the external \(N^2\)
is included in the polynomial factor.

The product in (1) is an entire one-periodic function of \(a\).
Therefore \(\Gamma_+\) has exactly the same complementary
integral as the original segment from \(1/2+ic\) to one.
This is an exact contour deformation with fixed endpoints, not
a replacement of a sampled root sum by an arc. Together with the
first path \(\Gamma_-\) already estimated in the first-half
assembly, it gives the original full observation.

**Corollary 2.** At complete ordinary colors,
\[
 Z_{34,N}(-2,-2)
 =\kappa_N^3N^{-3/2}\mathcal A e^{N\mathcal S}
                                  (1+O(N^{-1})),\qquad \mathcal A\ne0.
                                                               \tag{28}
\]
The asymptotic holds along all integer levels with both parity cases
retained and uses the original absolute action and Gaussian branch.
Indeed the first-half contribution has exactly (28), while (27)
is exponentially smaller and can be absorbed in its relative
\(O(N^{-1})\) error.

The uniform ordinary-color and fixed-jet statement (27) concerns
the complementary error. Equation (28) is stated at the complete
colors; no new full outside-color torus estimate is inferred from
it. The geometric calibration of \(\Re\mathcal S\) is the
existing original boundary-germ theorem. Insertion of this component
into a general long-filling family still requires its prescribed
whole real outside-color estimate and the original boundary assembly.
No arbitrary short-cluster or new knot-family conclusion is asserted
by this note alone.
