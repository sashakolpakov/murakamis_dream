# The complete transformed conditional source on the original three/four plateau

Research deduction, 7 November 2026. Fix the actual complete ordinary
three/four pair. Its complete conditional polynomial, with the outgoing
leg near the original right private coordinate, has a calibrated
incoming-plateau bound and a nonzero plateau-prefix packet. The proof
uses pointwise terminal current estimates after removing an explicit
nonzero endpoint coefficient. It never divides a bound for the signed
terminal polynomial. Every conditional row, including the revived
upper half, remains in the source. No new numerical evaluation is used.

## 1. The actual reference and the literal finite source

Retain the conventions and calibrated phases of
[the transformed-complement calibration](research_mixed_three_four_transformed_complement_calibration.md).
Write the actual shared leg, terminal transform leg, and right private
leg as
\[
 a_*=A+ic,\qquad t_*=T+ih_t,\qquad z_*=Z+ih_z.
 \tag{1}
\]
The original reference has
\[
 A\in(.278,.391),\quad -7/200<c<0,\quad
 T\in(.246,.350),\quad h_t\in(-.108,-.020),
 \quad .349<Z<.350,\quad -137/4000<h_z<-1/30.
 \tag{2}
\]
The last two bounds and the action calibration refer to the fixed
saved ordinary-pair reference, not to every point in its containing
rectangles. Put
\[
 P=[11/50,9/20],\quad \kappa_*=1/2500000,\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iz},\quad r=e^{-2\pi i/N}.
\]
The exact conditional polynomial and its original rows are
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}R_{N,j}(a,z),\qquad
 R_{N,j}(a,z)=\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
 \quad p_j(V)=(rV;r)_j,\quad P_j=(r;r)_j.
 \tag{3}
\]
There is no support restriction in (3) at the nonphysical value
\(z=z_*\). In particular all \(j\ge\lceil N/2\rceil\),
including the even-level half row, are present.

The plateau part of the exact transformed prefix is
\[
 f_{P,N}(w,z)=N\int_{11/50+ic}^{9/20+ic}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},e^{-2\pi iz})\,da.
 \tag{4}
\]
Its coefficient is exactly \(N\). There is no \(\kappa_N\),
right endpoint coefficient, final Gram transform, or outgoing
Fourier halfweight in (3)--(4).

Use the original primitives to define
\[
\begin{split}
 Q(t;a,z)&=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat,\\
 E_{\rm end}(z)&=S(z)-\frac{\pi i}{2}(z-z^2),\\
 \mathcal P_{34}(w,z)&=\operatorname{stat}_{a,t}
              [\mathcal T_0(a,w)+Q(t;a,z)].
\end{split}                                                        \tag{5}
\]
The branch in the last line is the original branch through
\((a_*,t_*)\) at \((w,z)=(-2,z_*)\).
Write \(P_* =\Re\mathcal P_{34}(-2,z_*)\).
The already proved exact action split and its analytic calibration give
\[
 M=P_*+\Re E_{\rm end}(z_*),\qquad M>27/10,
 \qquad \Re E_{\rm end}(z_*)<89/100,
 \qquad P_*>181/100.
 \tag{6}
\]
The actual stationary equation is
\(\mathcal T_0'(a_*,-2)+\mathcal P_1'(a_*)=0\), where
\(\mathcal P_1\) is the original complete terminal-four phase.

## 2. Removing only a known nonzero pointwise factor

Let \(\mathfrak P_N\) and \(\Delta_N\) be the exact original
marked factorial and quadratic mark, and set
\[
 D_N(z)=\Delta_N(z)^{-1}\mathcal C_N(z,-2),\qquad
 R_N(t;a,z)=e^{2\pi iNat}
 \frac{\mathfrak P_N(a+t)\mathfrak P_N(z+t)}
      {\mathfrak P_N(a)\mathfrak P_N(t)^3\mathfrak P_N(z)}.
 \tag{7}
\]
The exact difference equation gives
\(R_N(j/N;a,z)=R_{N,j}(a,z)\) whenever the displayed factorial
chart is regular. Equation (3) of
[the reduced terminal currents](research_mixed_terminal_four_reduced_currents.md)
is the pointwise identity
\[
       \widehat{\mathcal J}_N(a;z,t,-2)=D_N(z)R_N(t;a,z).
 \tag{8}
\]
The complete endpoint packet proves on a fixed neighborhood of \(z_*\)
\[
 D_N(z)=N^{-3/2}e^{i\pi z/2}A_C(z,-2)
                  e^{NE_{\rm end}(z)}(1+O_{\rm hol}(N^{-1})),
 \qquad A_C\ne0.
 \tag{9}
\]
Thus \(D_N\) is nonzero there for every sufficiently large \(N\),
with both parities. Division in (8) is an exact division of functions;
(9) supplies its uniform upper and lower bounds. No inequality for
the integrated or summed \(\mathcal V_{1,N}\) is divided.

For \(a=x+ic\), \(x\in P\), and
\(\Re t\in[.15,.5]\), \(|\Im t|\le.12\), all factorials
in (7) lie in their original regular strips:
\[
 \Re(a+t)\in[.37,.95],\qquad
 \Re(z_*+t)\in(.499,.850),\qquad
 \Re a,\Re z_*,\Re t\in(0,1).
 \tag{10}
\]
These statements hold on a fixed compact neighborhood, so include
half-grid perturbations and small complex changes in \(z\).
The exact source has the uniform symbol
\[
 R_N(t;a,z)=N^{-3/2}b(a,t,z)e^{NQ(t;a,z)}
                       (1+O_{\rm hol}(N^{-1})),
 \tag{11}
\]
where
\[
 b(a,t,z)=e^{i\pi t/2}
 \frac{\sqrt{2\sin\pi(a+t)}\sqrt{2\sin\pi(z+t)}}
 {(2\sin\pi a)^{1/2}(2\sin\pi t)^{3/2}
                         (2\sin\pi z)^{1/2}}\ne0.
 \tag{12}
\]
All roots and logarithms are the original ones. The factor
\(e^{i\pi z/2}A_C\) in (9) cancels exactly from the reduced
terminal symbol; this fixes the order-one mark in (12).

## 3. The exact central sum, its joins, and its aliases

Define integer cuts
\[
 L_N=\lceil3N/20\rceil,\qquad H_N=\lceil N/2\rceil-1,
 \qquad \alpha_N=(L_N-1/2)/N,
 \qquad \beta_N=(H_N+1/2)/N.
 \tag{13}
\]
For odd \(N\), \(\beta_N=1/2\); for even \(N\),
\(\beta_N=1/2-1/(2N)\). The low and high sums are respectively
\(0\le j<L_N\) and \(H_N<j<N\). Thus the three pieces
partition (3) exactly.

For a holomorphic function \(F\) on the central rectangle put
\(K_N(t)=(1-e^{-2\pi iNt})^{-1}\), \(h_-=-.12\),
and \(h_+=.12\). Let the following oriented three-sided paths
have the same half-grid endpoints:
\[
\begin{split}
 \Gamma_0&:\alpha_N\longrightarrow\alpha_N+ih_t
       \longrightarrow\beta_N+ih_t\longrightarrow\beta_N,\\
 \Gamma_-&:\alpha_N\longrightarrow\alpha_N+ih_-
       \longrightarrow\beta_N+ih_-\longrightarrow\beta_N,\\
 \Gamma_+&:\beta_N\longrightarrow\beta_N+ih_+
       \longrightarrow\alpha_N+ih_+\longrightarrow\alpha_N.
\end{split}
\]
Residues on the full counterclockwise rectangle, followed by Cauchy's
theorem for its constant term, give exactly
\[
 \sum_{j=L_N}^{H_N}F(j/N)=N\left\{
    \int_{\Gamma_0}F(t)\,dt
   +\int_{\Gamma_-}(K_N(t)-1)F(t)\,dt
   +\int_{\Gamma_+}K_N(t)F(t)\,dt\right\}.
 \tag{14}
\]
This keeps three constant currents and six alias currents. In
particular the main horizontal coefficient is \(+N\), while the
upper alias runs from right to left. On either vertical side,
\[
 K_N(\alpha_N+iv)=K_N(\beta_N+iv)
                  =(1+e^{2\pi Nv})^{-1}.
 \tag{15}
\]
The lower and upper penalties are therefore exactly \(2\pi|v|\)
up to bounded factors, including the value \(1/2\) at zero.
There is no missing cut current or parity-dependent sign.

To bound (14), restrict the original pointwise terminal profiles to
\(e=z_*\). This restriction is allowed in both flattened \(t\)
faces and the \(t\)-single aliases at the actual private height.
All their real variables remain in their full original intervals.
The actual-reference comparisons, including Condition C, are discharged
by Section 1 of
[the full unselected plateau theorem](research_mixed_full_unselected_plateau.md).
This use neither places \(z_*\) in an ordinary external-input domain
nor assumes a corresponding ordinary two-leg root.

Put
\[
 B_V(x)=\Re\mathcal P_1(a_*)+
          \Re\mathcal P_1'(a_*)(x-A)-\kappa_*(x-A)^2,
 \qquad B_C(x)=B_V(x)-\Re E_{\rm end}(z_*).
 \tag{16}
\]
The main horizontal profile is at most \(B_C(x)\), with the
stronger actual-height quadratic loss supplied by
\(-\Re\widehat{\mathcal F}_1''\succ(\pi/100)I\).
Both flattened \(t\)-faces and both horizontal \(t\)-aliases
have rate at most \(B_C(x)-1/20000\). Convexity in the
\(t\)-height reduces each ordinary vertical join to its real
and actual-height ends; the latter is a horizontal boundary with
the same strict margin. For an alias side, subtracting the linear
penalty on each sign half leaves the same convexity. Its endpoint
values are the real face and the corresponding outer alias.
This proves the same gap for all eight nonmain currents in (14).

Here the gap is a pointwise phase statement before integration, obtained
from (8)--(9). It is not a bound on an individual private-index piece
deduced from the complete terminal sum. Uniform symbols, half-grid
rounding, and a sufficiently small \(z\)-neighborhood consume only
one arbitrarily small common tolerance.

## 4. All low rows and all revived high rows

For physical \(u=j/N\) use the complete absolute-row rate
\[
 E(u;a,z)=I_a(u)+I_z(u)-3J(u)-2\pi c u,
 \qquad I_v(u)=\int_0^u\log|1-e^{-2\pi i(v+s)}|\,ds.
 \tag{17}
\]
The uniform numerator and sine-factorial estimates give
\(\log|R_{N,j}|\le NE(j/N;a,z)+O(\log N)\), uniformly
through \(j=0,N-1\). This includes all zeros rather than dividing
by a product. Here \(c,h_z<0\) in fact keep the two numerator
circles strictly inside the unit disk.

On \(0<u\le.15\), equation (17) of
[the asymmetric contour proof](research_mixed_horizontal_asymmetric_contour.md)
gives \(\partial_uE>1/2\) for independent real parts in \(P\)
and the stated height bounds. Its proof is the two sine-ratio
inequalities, each greater than two, with the original first chirp
retained. It has no ordinary-reference correlation premise. Consequently
the whole low sum is bounded by the flattened \(t=.15\) profile,
already at most \(B_C(x)-1/20000\).

The independent-target theorem in
[the complete right-tail bound](research_mixed_right_tail_endpoint_bound.md)
applies with \(a=x+ic\), \(z=z_*\): both real parts lie in
\(P\) and both heights have modulus less than \(.108\). It gives
\[
       E(u;a,z_*)\le\max\{E(1/2;a,z_*),E(1;a,z_*)\},
                        \qquad 1/2\le u\le1.
 \tag{18}
\]
The half value is exactly the flattened terminal profile after
subtracting \(\Re E_{\rm end}(z_*)\), hence has the same
\(1/20000\) gap below \(B_C(x)\). This includes every revived
row, without the old terminal triangle \(j+Nz_*<N\).
The other value is simply
\[
                  E(1;a,z_*)=-2\pi c<11/50,
 \tag{19}
\]
by the full-circle logarithmic integral and \(|X|,|Y_*|<1\).
Equations (14)--(19), with at most \(N\) real tail rows, prove
the standalone bound
\[
 |C_{1,N}(e^{-2\pi i(x+ic)},Y_*)|
 \le C_\tau N^{B_\tau}
       e^{N\{\max(B_C(x),-2\pi c)+\tau\}},
                         \qquad x\in P.
 \tag{20}
\]
Its nonmain central currents and its low/half-controlled rows have
the strict margins above. The second branch in (20) has not been
discarded merely because the signed sum has a central packet.

## 5. Calibrating the last branch with the complete first cap

The original exact cap is
\[
 U_{0,N}(w,X)=\sum_{k<N}b_k(w)p_k(X),\qquad
 b_k(w)=\Delta_N(k/N)^{-1}\mathcal C_N(k/N,w).
 \tag{21}
\]
[The seam source ceiling](research_mixed_cap_seam_source_bounds.md),
Theorem 1 for its type-one absolute coefficient sum, includes every
true private endpoint and gives
\(\sum|b_k(w)|\le\operatorname{poly}(N)e^{N(433/500+\tau)}\)
on a small fixed ordinary-color disk. The complete arc product estimate
and its disk maximum principle give
\[
 \sup_{|X|\le1}|p_k(X)|
       \le\operatorname{poly}(N)e^{N(L(k/N)+\tau)},
 \qquad L(t)=-2J((1-t)/2)<1/3.
\]
These are the same finite product bounds used in
[the transformed complementary source](research_mixed_three_four_transformed_complement.md),
Section 3. Thus, on the whole closed unit disk,
\[
 |U_{0,N}(w,X)|
      \le C_\tau N^{B_\tau}e^{N(433/500+1/3+\tau)}.
 \tag{22}
\]
Combining this bound with (19) pays the entire last-controlled branch
in (18), because
\[
       433/500+1/3+11/50=2129/1500<3/2<P_*.
 \tag{23}
\]
No estimate for a partial endpoint Newton sum is used in (22).

For the other branch and all central profiles use the stronger complete
cap plane from
[first-cap plateau completion](research_mixed_first_cap_plateau_completion.md):
\[
 B_U(x)=\Re\mathcal T_0(a_*,-2)+
        \Re\mathcal T_0'(a_*,-2)(x-A)-\kappa_*(x-A)^2.
\]
The original reference equation and (6) give exactly
\[
                  B_U(x)+B_C(x)=P_*-2\kappa_*(x-A)^2.
 \tag{24}
\]
Since \(|x-A|<1\), the large reserve in (23) also pays the
quadratic term on the right of (24).

**Theorem 1 (complete plateau source bound).** For every \(\tau>0\),
there are fixed sufficiently small neighborhoods of \(w=-2\) and
\(z=z_*\), and constants such that for all \(x\in P\),
all sufficiently large \(N\) of either parity,
\[
 |U_{0,N}(w,e^{-2\pi i(x+ic)})
       C_{1,N}(e^{-2\pi i(x+ic)},e^{-2\pi iz})|
 \le C_\tau N^{B_\tau}
           e^{N\{P_*-2\kappa_*(x-A)^2+\tau\}}.
 \tag{25}
\]
At the center parameters, every nonmain \(t\)-current and every
physical tail has a uniform additional strict gap; after tolerances
one may take \(1/100000\). All fixed \(w,z\) derivatives satisfy
the upper bound with their polynomial costs on smaller neighborhoods.

For completeness, (18) continues directly on a small \(z\)-disk
inside \(P+i(-.108,0)\); the two endpoint values are continuous.
The central phase bounds and cut gaps persist by compact continuity.
The whole cap plane and (22) retain their original color neighborhoods.
Choose these neighborhoods after fixing the total tolerance, and then
take \(N\) large. This proves (25) on an actual ambient neighborhood
in \((w,z)\), so its derivative assertion follows by Cauchy's formula.
It is not obtained by differentiating a value-only inequality.

## 6. A nonzero holomorphic packet for the actual plateau prefix

**Theorem 2.** On a fixed neighborhood of \((-2,z_*)\),
the exact plateau integral (4) has the packet
\[
 f_{P,N}(w,z)=N^{-3/2}\mathcal A_P(w,z)
          e^{N\mathcal P_{34}(w,z)}(1+O_{\rm hol}(N^{-1})),
                         \qquad \mathcal A_P\ne0.
 \tag{26}
\]
The normalized error has every fixed mixed derivative uniformly on
smaller neighborhoods. No ordinary normal is replaced by evaluation
at a Fourier node. All incoming cap sums and conditional rows remain
in (4).

Here is the source proof, including the contour through the moved
critical point. Theorem 1 and its stronger central horizontal loss
remove, with a fixed exponential margin, the part of the exact
two-current main integral outside a small real product box about
\((A,T)\) at heights \((c,h_t)\). The physical tails and the eight
other \(t\)-currents have the already proved strict gap. On the
small box the complete first cap has its original holomorphic packet
\[
 U_{0,N}(w,e^{-2\pi ia})=N^{-1}\mathcal B_0(a,w)
           e^{N\mathcal T_0(a,w)}(1+O_{\rm hol}(N^{-1})),
 \qquad\mathcal B_0\ne0.
\]
Together with (11), this is a symbol for the exact main integrand,
not a relative approximation substituted into an uncontrolled outer sum.

The original open-word accretive Hessian, followed by the original
endpoint Schur reductions, makes the negative Hessian of
\(\mathcal T_0+Q\) in \((a,t)\) accretive at the reference.
It supplies a holomorphic critical point \((a^\#,t^\#)(w,z)\)
and a nonzero Gaussian determinant on a smaller neighborhood. Translate
the two finite local main segments by
\(a^\#-a_*\) and \(t^\#-t_*\), sequentially by the
one-variable Cauchy theorem. Retain the four swept product-boundary
faces. Each lies near the old box boundary, where the center phase
has a fixed strict loss. Compact continuity, with the parameter
neighborhood chosen sufficiently small, keeps every swept face
exponentially below \(\Re\mathcal P_{34}(w,z)\).
The translated product has the moved saddle at its original interior
real coordinates, and the negative real Hessian stays positive.

The two-dimensional Gaussian now gives
\[
 \mathcal A_P(w,z)=
 \frac{2\pi\,\mathcal B_0(a^\#,w)b(a^\#,t^\#,z)}
 {\sqrt{\det[-\partial_{(a,t)}^2
               (\mathcal T_0(a,w)+Q(t;a,z))]_{(a^\#,t^\#)}}}.
 \tag{27}
\]
The determinant square root is its original accretive Gaussian branch.
The leading orientation is positive in both real coordinates. The
normalization is exactly
\[
             N^2\,N^{-1}\,N^{-3/2}\,(2\pi/N)
                            =2\pi N^{-3/2}.
 \tag{28}
\]
One factor \(N\) is (4), and the other is (14). Both parity
cuts contain the same saddle and affect only the paid boundary region.
After \(N^{-1/2}\) rescaling on a symmetric local box, the linear
symbol and cubic phase corrections are odd; their integrals vanish.
The uniform quartic remainder gives the stated relative \(O(N^{-1})\).
Holomorphy and nested Cauchy estimates give all normalized fixed mixed
jets. This proves (26).

The same argument with \(a\) held near \(a_*\) also gives a
complete local \(C_1\) packet of power \(N^{-1}\), with coefficient
\(\sqrt{2\pi}\,b(a,t^\#,z)/\sqrt{-Q_{tt}(t^\#;a,z)}\).
For its last rows, (22)--(23) and the nonzero original cap packet
imply the strict phase comparison at the reference; continuity keeps
it locally. This local statement is not a moving saddle theorem on
every independent incoming plateau target.

## 7. The remaining first-path estimates

The result concerns the central incoming plateau and fixed outgoing
private-leg neighborhood. The exact first incoming path also contains
the initial seam segment, real small-angle segment, left attenuated
taper, and right strip leading to \(1/2+ic\). Their estimates must
be proved for the transformed source \(U_0C_1(\cdot,Y)\) at this
fixed outgoing leg. A bound for \(U_0\mathcal V_1\) on those
regions is not itself such a proof.

In particular outside the plateau one must retain the actual incoming
height, its full complex affine marginal, the complete low-row source,
and all retained \(t\)-joins and aliases. On the right strip the
revived high rows require the independently extended endpoint theorem;
on the left taper the incoming height changes and its row/contour
comparison remains a distinct obligation. Near the initial seam, an
exact finite-source bound or identity is still needed. None of these
are hidden in a division by the whole signed terminal factor.

The separately calibrated complementary path \(\Gamma_+\) already
has its strict transformed-source gap near \(z_*\). Combining it
with (26) proves a whole-prefix packet only after the remaining
first-path pieces have been paid on the same action scale. The final
Gram transform, arbitrary following-leg reference families, and
arbitrary short-word closure are further statements, not consequences
of this plateau theorem.
