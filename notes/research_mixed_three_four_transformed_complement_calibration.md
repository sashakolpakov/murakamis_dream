# A calibrated transformed remainder at the original three/four pair

Research deduction, 7 November 2026. The exact inverse-boundary
transform of the complementary incoming contour has a strict gap
at the last private leg of the original complete ordinary pair.
The proof sharpens its numerator bound on a smaller outgoing disk,
then bounds the actual complex right-endpoint action using only
previously saved enclosures and elementary inequalities. No new
source, root, or numerical evaluation is used.

This is one remainder of the exact retained-leg prefix. The
transformed first path, a whole-prefix packet, and a uniform estimate
at the following-leg references of longer words remain separate.

## 1. Exact source and the two distinct cut phases

Use the original notation of
[the transformed complementary contour](research_mixed_three_four_transformed_complement.md):
\[
\begin{split}
 f_{34,N}(w,Y)&=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 f_{+,N}(w,Y)&=N\int_{\Gamma_+}U_{0,N}(w,X)C_{1,N}(X,Y)\,da,
       \qquad X=e^{-2\pi ia},\\
 \Gamma_+&:[1/2+ic,1/2]\cup[1/2,1],\qquad -7/200<c<0.
\end{split}                                                        \tag{1}
\]
Here
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad r=e^{-2\pi i/N}.
                                                                    \tag{2}
\]
Every original row and zero is retained. Both functions in (1)
are polynomials of degree less than \(N\) in each of \(w,Y\).
If the ordinary complementary polynomial has coefficient row
\(\mathbf e_+(w)^T\), then exactly
\[
 (f_+(w,r^j))_{j=0}^{N-1}
       =(\kappa_N^3N)^{-1}\mathbf e_+(w)^TS^{-1}.        \tag{3}
\]
Thus (1) contains no final Gram matrix. In contrast the retained
phase \(H_{34}\) of
[the arbitrary-letter phase class](research_mixed_actual_prefix_arbitrary_letter_phase_class.md)
belongs to the row \(b_L^TB_3\Gamma B_4\Gamma\).
If \(\mathcal P_{34}(z)\) is the pre-Gram phase defined below,
their relation is
\[
 H_{34}(b)=\operatorname{stat}_z[\mathcal P_{34}(z)+G(z,b)],
 \qquad G(z,b)=g(z+b)-2g(z)-2g(b)+2\pi izb.              \tag{4}
\]
No inequality for one representation is silently assigned to the other.

Write
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad
 E_{\rm end}(e)=S(e)-\frac{\pi i}{2}(e-e^2),\\
 Q(s;a,z)&=g(s+a)+g(s+z)-3g(s)-g(a)-g(z)+2\pi ias,\\
 \mathcal P_{34}(z)&=\operatorname{stat}_{a,s}[T_0(a)+Q(s;a,z)].
\end{split}                                                        \tag{5}
\]
All primitives and critical branches are original. The first cap
\(T_0\) already eliminates its original private leg and endpoint
coordinate. Equivalently the last line eliminates four variables
in the original unreduced action. At the complete ordinary pair,
let \(z_*=f_*\) be its right private leg and \(v_*\) its right
ordinary endpoint coordinate. The original six-variable action
splits exactly as
\[
 \mathcal A_{34}^*=\mathcal P_{34}(z_*)+E_{\rm end}(z_*),
 \qquad M=\Re\mathcal A_{34}^*>27/10.                    \tag{6}
\]
Indeed the saved action is
\(T_0(a)+P_1(f,b,v)+J(a+b)-J(a)-J(b)+i\pi ab-g(b)\).
Substituting \(P_1=E_{\rm end}(f)+g(f+b)-g(b)-g(f)\)
gives (5)--(6), with \(s=b\). This checks every own-factor
and chirp in the split.

There is no alternating endpoint gauge: if
\(S_j=\prod_{k=1}^j2\sin(\pi k/N)\), then
\[
 P_j=i^j q^{-j(j+1)/2}S_j,\qquad
 \frac{H_N(w,r^{-j})}{P_j}
   =(-i)^jq^{j(j+1)/2}
      \sum_{\ell=0}^j\frac{q^{j\ell}e_\ell(w)}{S_\ell S_{j-\ell}}.
                                                                    \tag{7}
\]
The factor before the sum is the original \(\delta_j^{-1}\).
Its limiting phase is precisely the quadratic term in
\(E_{\rm end}\), not that term plus \(i\pi e\).

The original full Hessian is accretive after changing sign.
Its principal block in the four eliminated variables is therefore
nonsingular. The implicit function theorem defines (5), with its
original constant, on a fixed neighborhood of \(z_*\), and also
for \(w\) near \(-2\) using the original ordinary-color cap.
This assertion concerns the selected critical action; it does not
assert that the whole finite prefix already has that asymptotic.

## 2. A smaller-disk bound for every outgoing numerator

Put \(L(t)=-2J((1-t)/2)\). For \(0\le R\le1\), the function
\(\log|1-Re^{i\theta}|\) is symmetric about \(\theta=\pi\)
and decreases with distance from that point. Differentiating the
integral with respect to the starting angle, or comparing its two
end values, therefore proves
\[
 \int_0^t\log|1-Ye^{-2\pi iu}|\,du
 \le\int_{-t/2}^{t/2}\log|1+R e^{2\pi iu}|\,du,
 \qquad R=|Y|.                                         \tag{8}
\]
For \(0\le t\le1/2\), the interval on the right has
\(|u|\le1/4\), and
\[
 \frac{|1+R e^{2\pi iu}|^2}{|1+e^{2\pi iu}|^2}
   =R+\frac{(1-R)^2}{4\cos^2\pi u}
   \le\frac{1+R^2}{2}.                                \tag{9}
\]
When \(R\le5/6\), equations (8)--(9) give
\[
 I_Y(t):=\int_0^t\log|1-Ye^{-2\pi iu}|\,du
       \le L(t)-\frac{2t}{25}\qquad(0\le t\le1/2).    \tag{10}
\]
Here
\(\tfrac12\log(72/61)>11/133>2/25\), by
\(\log(1+x)>2x/(2+x)\). At \(R=0\) the same inequality
follows from (8)--(9). No product is divided at a zero.
For \(t\ge1/2\) retain the old bound \(I_Y(t)\le L(t)\).
For example it follows from the centered-arc maximum at \(R=1\)
and the subharmonic maximum principle in \(Y\).

Use the scalar from the completed complementary proof,
\[
 D(t)=L(t)-J(1/2-t)-3J(t),\qquad 0\le t\le1/2.
\]
Its already proved inequalities are
\[
 D''\le-2\pi\sqrt3,\quad D'(1/4)=\log\cos(\pi/8),\quad
 -1/10<D'(1/4)<0,
 \quad D(1/4)<\frac7{40}-\frac3{512}+\frac{73}{125}.
                                                                    \tag{11}
\]
The quadratic support for \(D(t)-2t/25\), using
\(4\pi\sqrt3>20\), now yields
\[
 \max_{0\le t\le1/2}[D(t)-2t/25]
 <\frac7{40}-\frac3{512}+\frac{73}{125}
      -\frac1{50}+\frac{81}{50000}<\frac{147}{200}.
                                                                    \tag{12}
\]
The last comparison uses \(3/512>281/50000\).

The full cap ceiling on \(\Gamma_+\) is
\(B_0=1549/1500\). On the real part of that path, (10)--(12)
bound every lower-half transform row by \(B_0+147/200\).
On its vertical part, set \(\delta=-2\pi\Im a<11/50\).
The original exact radial/chirp comparison gives, for \(t\le1/3\),
\[
 D_\delta(t)-D(t)<11/300+7/1920.                         \tag{13}
\]
Here \(D_\delta=L-3J+I_{1/2,-\delta/(2\pi)}+\delta t\).
The same source proves \(D_\delta'<-1/3\) on
\([1/3,1/2]\); hence \(D_\delta-2t/25\) is decreasing
there too. Thus (12)--(13) include all lower-half rows.
The old upper-half row ceilings are unchanged and are at most
\(793/500\). Consequently the complete rate on this smaller disk is
\[
 B_0+147/200+11/300+7/1920
     =\frac{86783}{48000}<\frac{226}{125}.              \tag{14}
\]
This retains the complete vertical segment, every transform index
including zero and \(N-1\), the original chirp, and both level parities.

Uniform numerator-product upper estimates and the denominator
factorial estimates therefore prove, for every \(\tau>0\),
\[
 \sup_{\substack{w\in[-2,2]\\|Y|\le5/6}}
 |\partial_w^k f_{+,N}(w,Y)|
 \le C_{k,\tau}N^{B_{k,\tau}}
              e^{N(226/125+\tau)}.                    \tag{15}
\]
Markov is applied to the complete cap before summing its transform
rows. Fixed outgoing derivatives have the same estimate on compact
subdisks. The original small-complex-color version of the cap
ceiling gives (15) near \(w=-2\) as well, with an arbitrarily
small additional rate tolerance. Equivalently polynomial
Bernstein growth from the whole real interval supplies that
extension after shrinking the fixed color disk. This passage
does not replace any normal observation by physical node values.

## 3. The complex endpoint action is less than \(89/100\)

Only two previously completed saved records are used here. The
[six-root action record](../repro/results/research-mixed-three-four-half-face-witnesses-attempt01.json)
has SHA256
`fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70`.
Its displayed `coordinate_boxes[3]`, `coordinate_boxes[5]`, and
`original_action` directly imply
\[
\begin{split}
 349/1000&<x:=\Re z_*<350/1000,\\
 -137/4000&<y:=\Im z_*<-1/30,\\
 225/1000&<p:=\Re v_*<226/1000,\qquad
 0<q:=\Im v_*<93/2500,\qquad M>27/10.
\end{split}                                                        \tag{16}
\]
For example the saved real interval for \(z_*\) starts with
\((.34940341045,.34940341232)\), its height interval with
\((-.03422896383,-.03422896196)\), and the saved \(v_*\)
intervals with \((.22574508157,.22574508344)\) and
\((.03719403003,.03719403190)\). These abbreviated intervals
are explanatory; (16) follows from the full saved decimal bounds.
The saved original logarithmic equations identify
\(v_*=u_c(z_*)\).

The [completed seam replay](../repro/results/research-mixed-cap-seam-source-bounds-replay.json),
SHA256
`8d907c890073955f7e1122abc78f1334ab00a885959d839316d3852e2a64f3f8`,
contains
\[
 \lambda(7/20)<8641/10000,\qquad
 -1/100<\lambda'(7/20)<0,
 \qquad \lambda(x)=\Re S(x).                            \tag{17}
\]
Its saved central values begin respectively
\(.864089941023\) and \(-.004747972221\), with their full
outward error radii retained in the record. No action is evaluated
again to use (16)--(17).
Real concavity and the supporting tangent at \(7/20\) give
\[
             \lambda(x)<8642/10000.                    \tag{18}
\]

The whole segment \(x+i[y,0]\) is inside the established
\(E_{\rm cap}=[.27,.49]+i[-.055,.04]\). On this entire
rectangle, the [endpoint packet](research_mixed_endpoint_cap_rectangle.md),
equation (9), puts the original branch in
\(.17<\Re u_c<.28\), \(.001<\Im u_c<.1\), and
\(0<\Re(e-u_c)<1/2\), with zero logarithmic lift.
Thus no branch or chamber is changed along the segment.
The [complex endpoint curvature](research_mixed_cap_early_taper_complex_profiles.md),
equation (4), proves \(-\Re S''>0\) there.
Since \(E_{\rm end}''=S''+i\pi\), the function
\(v\mapsto\Re E_{\rm end}(x+iv)\) is strictly convex.

At the saved endpoint, original stationary differentiation gives
\[
 \Im E_{\rm end}'(z_*)
 =\arctan\!\left(\tanh(\pi(q-y))\cot(\pi(x-p))\right)
          +\pi(x+p-1/2)<3/4.                           \tag{19}
\]
Here are elementary witnesses for the last inequality. We have
\(x-p>123/1000\), and \(\pi>157/50\) implies
\(\pi(x-p)>77/200\). Since \(\tan t>t+t^3/3\),
\[
 \tan(\pi(x-p))>77/200+(77/200)^3/3>2/5,
 \qquad \cot(\pi(x-p))<5/2.
\]
Also
\[
 \pi(q-y)<15719/70000
     <494/2187=2/9+(2/9)^3/3<\operatorname{arctanh}(2/9).
\]
Hence the arctangent argument in (19) is less than \(5/9\).
The alternating integral expansion and \(x+p-1/2<19/250\)
give
\[
 \Im E_{\rm end}'(z_*)
 <\frac59-\frac{(5/9)^3}{3}+\frac{(5/9)^5}{5}
       +\frac{22}{7}\frac{19}{250}
 =\frac{30055}{59049}+\frac{209}{875}<\frac34.           \tag{20}
\]

For a convex differentiable function, the tangent at its lower
endpoint lies below its value at zero. Applying this to the
vertical restriction, and keeping \(y<0\), gives
\[
\begin{split}
 \Re E_{\rm end}(z_*)-\lambda(x)
 &\le |y|\Im E_{\rm end}'(z_*)\\
 &<\frac{137}{4000}\frac34.
\end{split}
\]
Together with (18), this proves
\[
 \boxed{\quad \Re E_{\rm end}(z_*)
      <\frac{8642}{10000}+\frac{411}{16000}
      <\frac{89}{100},\qquad
      \Re\mathcal P_{34}(z_*)>\frac{181}{100}.\quad}    \tag{21}
\]
The first bound is for the original complex endpoint action,
not an extrapolation of the real seam ceiling \(433/500\).

## 4. A genuine normalized remainder gap, with its scope

By (16),
\(2\pi\Im z_*<-\pi/15<-1/5<-\log(6/5)\).
Therefore \(|e^{-2\pi iz_*}|<5/6\), strictly. Equations
(14) and (21) show the raw gap
\[
 \Re\mathcal P_{34}(z_*)-226/125>1/500.                 \tag{22}
\]
Choose a sufficiently small fixed bidisk about \((w,z)=(-2,z_*)\).
It remains inside \(|e^{-2\pi iz}|<5/6\) and the original
holomorphic critical branch. Shrink it so the change in
\(\Re\mathcal P_{34}(w,z)\), together with the prescribed
source/color tolerances, spends less than \(1/2000\).
The polynomial factors in (15) can then be absorbed strictly
before \(1/1000\). On a smaller fixed bidisk, for every fixed
mixed derivative order,
\[
 \left|\partial_w^k\partial_z^\ell
   \left[e^{-N\mathcal P_{34}(w,z)}
                f_{+,N}(w,e^{-2\pi iz})\right]\right|
       \le C_{k,\ell}e^{-N/1000}                       \tag{23}
\]
for all sufficiently large integer levels, both parities included.
Holomorphy and fixed-radius Cauchy estimates are applied to the
normalized function in (23). No division by the finite source is used.
The exact factor \(\kappa_N^3N\) in (3) remains when this
prefix remainder is converted back to its ordinary observation.

This is an actual calibrated estimate for the complete inverse-S
complementary current near the saved ordinary-pair reference.
It neither proves a leading asymptotic for \(f_{34,N}\) nor
controls its first-path remainder \(f_-\). The following-leg
references for longer words are a different family; membership
of \(z_*\) in a containing typed disk does not promote (23)
to that family. A final Gram contraction, the type-four selected
factor, and any prescribed subsequent observation must still be
retained and estimated in their own source. No arbitrary short-word
or additional knot theorem follows from this remainder estimate alone.
