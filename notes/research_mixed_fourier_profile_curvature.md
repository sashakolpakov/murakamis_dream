# Curvature of the actual Fourier source bounds near the interface

Research proof, 7 November 2026. The full-period estimates retain each
source term's boundary index. That dependence gives more than the
correct value and first derivative at the reference: the central
profiles have a definite negative curvature in the real Fourier
variables. The other profiles remain strictly below them on a
specified smaller interval. All estimates below are analytic; no new
function values or numerical comparisons are used.

This establishes a local property of the actual source majorants.
It does not prove a bound on the complementary Fourier period or
stability under attachment.

## 1. The boundary incidence as a quadratic form

Write \(x_0=\xi+i\tau\) for the original alternating interface,

\[
 K=e^{2\pi i x_0},\qquad \rho=|K|,\qquad
 .18299<\xi<.18301,\qquad 3/5<\rho<5/8.
 \tag{1}
\]

The primitive occurring in the exact cardinal Fourier functions is

\[
 \ell_a(x)=2\pi ix(a-1/2)
 -\frac{\operatorname{Li}_2(e^{2\pi ix}e^{-2\pi ia})
              -\operatorname{Li}_2(e^{2\pi ix})}{2\pi i}.
 \tag{2}
\]

The linear term uses the displayed lift of \(x\). Put

\[
 X=e^{2\pi ix},\quad Z=Xe^{-2\pi ia},\qquad
 c(a,x)=\frac{-2\pi\Im Z}{|1-Z|^2},\qquad
 d(x)=\frac{2\pi\Im X}{|1-X|^2}.
 \tag{3}
\]

All variations in the next identity are real horizontal variations;
the imaginary parts of \(a,x\) are fixed. Direct differentiation gives

\[
 \ell_{aa}=-\frac{2\pi i Z}{1-Z},\qquad
 \ell_{ax}=\frac{2\pi i}{1-Z},\qquad
 \ell_{xx}=2\pi i\left(\frac{X}{1-X}-\frac{Z}{1-Z}\right),
\]
and therefore
\[
 \boxed{\quad -\Re d^2\ell_a(x)
       =c(a,x)(da-dx)^2+d(x)\,dx^2.\quad}
 \tag{4}
\]

Here \(d^2\ell\) denotes the second differential, whereas \(d(x)\)
is the scalar defined in (3). In particular the two-variable form
is positive whenever \(X\) is in the upper half-plane and \(Z\)
is in the lower half-plane.

Keep \(\Im x=\tau\) and let

\[
                   7/40\le\Re x\le3/16.
 \tag{5}
\]

Then \(d(x)>\pi\). Indeed
\(
 \sin(2\pi\Re x)>4/5
\)
and
\(
 \cos(2\pi\Re x)>3/8
\), so
\[
 \frac{d(x)}\pi>
 \frac{24/25}{1+25/64-9/20}
                  =\frac{1536}{1505}>1.
 \tag{6}
\]
The trigonometric comparisons follow from monotonicity on the
indicated first-quadrant interval, \(\sin(\pi/3)>4/5\),
and \(\cos(3\pi/8)>3/8\).
For every central-profile boundary leg used in Sections 2--3, its real part lies in
\([1/5,1/2]\). Hence
\(0<\Re a-\Re x<1/2\), and \(c(a,x)>0\), including all
of the original allowed imaginary heights.

## 2. The entire central profile of the prepared boundary function

Use the original prepared function
\[
 G_N(y)=v_N(-2)^TA_{3,N}A_{4,N}h_N(y),
 \qquad M=\Re\Phi_{\rm cap}(x_0,-2).
\]
Its [full-period bound](research_mixed_prepared_cap_full_period_profile_transport.md)
has central profile
\[
 P_{\rm m}(u;\theta)=B(u_t)+
   \Re R(u+ih;x_0+\theta),\quad
 u\in C_3=[.22,.5]\times[.2,.42]^2,
 \tag{7}
\]
where \(h\) is the actual critical height, \(B\) is the quadratic
supporting bound for the entire first cap, and
\[
 R(t,p,q;y)=V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(y),
 \qquad V(a,b)=g(a+b)-g(a)-g(b).
 \tag{8}
\]
In particular \(B''=-2\kappa_0<0\). The negative real Hessians
of the two \(V\) terms and of \(-g(p)\) are nonnegative on this
product, with the strict internal control proved in the original
source theorem. The chirp has zero real Hessian. Formula (4) shows
that, jointly in the three real indices and \(\theta\),
\[
                   -d^2P_{\rm m}\ \ge\ \pi\,d\theta^2
 \tag{9}
\]
whenever \(x_0+\theta\) satisfies (5).

At \((u,\theta)=(u_*,0)\), the internal gradient vanishes by
the original marginal cancellation. Put
\[
              p_{\rm cap}=\Re\partial_y\Phi_{\rm cap}(x_0,-2).
\]
Integrate (9) on the straight segment from \((u_*,0)\) to
\((u,\theta)\). All intermediate indices and Fourier variables
remain in their stated convex domains. This proves
\[
 \boxed{\quad
  \sup_{u\in C_3}P_{\rm m}(u;\theta)
       \le M+p_{\rm cap}\theta-\frac\pi2\theta^2.
       \quad}
 \tag{10}
\]
No assertion that the maximizing index stays in the interior is
needed for this inequality.

The same proof applies to the central profiles of every fixed
three/four prefix of length at least two ending in four, as defined
in the [coherent main-sheet theorem](research_mixed_fourier_prefix_coherent_main_sheet.md).
Their first-cap plane is unchanged as the output moves; the residual
is a sum of the same nonnegative pair forms, own-leg terms and one
outgoing incidence (2). All outer real legs are in \([.22,.45]\).
Thus (10), with the actual action and output momentum of that word,
has the same output-curvature constant \(\pi\). For a general
prefix this controls its central sheet only, not the whole finite sum.

## 3. The two Fourier variables of the complete paired kernel

The [full paired-kernel source](research_mixed_paired_kernel_full_period_profile_transport.md)
has central phase
\[
 \begin{split}
 F(s,t,p,q;x,y)={}&B_0(s,t;x)+V(t,p)+V(p,q)-g(p)\\
                &+2\pi itp+\ell_q(y),\\
 B_0(s,t;x)={}&g(s+t)-g(t)+\ell_s(x).
 \end{split}
 \tag{11}
\]
Its four real index intervals are
\([
 1/4,1/2]\), \([1/5,9/20]\), and two copies of
\([1/5,21/50]\); its heights are exactly those in the
[enlarged-rectangle theorem](research_mixed_contracted_pair_enlarged_rectangle.md).
Both \(x,y\) have height \(\tau\) and real parts in (5).

We claim the joint horizontal Hessian satisfies
\[
             -\Re d^2F\ \ge\ \frac\pi4(dx^2+dy^2).
 \tag{12}
\]
The only additional issue beyond (4) is the first sum \(g(s+t)\).
If \(\Re(s+t)\ge1/2\), its negative real Hessian is
nonnegative, and (12) follows at once from (4), (6) and the
remaining pair forms.

Suppose \(\Re(s+t)<1/2\). Set
\(C=\Re\cot\pi(s+t)\), \(T=\Re\cot\pi t\), and
\(a=c(s,x)/\pi\). The elementary estimates of the
enlarged-rectangle theorem hold for the entire external interval
(5), not only at \(x_0\):
\[
        0<C<1/5,\qquad T>4/5,\qquad a>54/125.
 \tag{13}
\]
For completeness the last bound uses
\(\Re s\in[1/4,3/10)\),
\(12/25<\rho e^{2\pi\Im s}<7/10\), and
\(\pi/8\le2\pi(\Re s-\Re x)<\pi/4\).
Consequently \(\sin\theta>3/8\), \(\cos\theta>7/10\),
and the denominator of (3) is less than \(5/6\).
These give \(a>54/125\) exactly as in that theorem.

Using \((ds+dt)^2\le(4/3)ds^2+4dt^2\), equations
(4), (6) and (13) give
\[
 \begin{split}
 -\Re d^2 B_0-\frac\pi4dx^2
 &\ge\pi\left\{
    \frac{54}{125}(ds-dx)^2+\frac34dx^2
                       -\frac4{15}ds^2\right\}.
 \end{split}
 \tag{14}
\]
The two-variable form in braces is positive definite. Its
\(ds^2\) coefficient is \(62/375\), and its determinant is
\[
 \frac{54}{125}\left(\frac34-\frac4{15}\right)
                     -\frac4{15}\frac34=\frac{11}{1250}>0.
 \tag{15}
\]
The discarded \(dt^2\) remainder is nonnegative. All remaining
terms of (11) have nonnegative negative real Hessian, and the
outgoing incidence contributes more than \(\pi dy^2\).
This proves (12) throughout the complete enlarged domain.

Let \(M_{34}\) be the original paired critical rate, and let
\(p_3=\Re\Phi_{34,x}(x_0,x_0)\),
\(p_4=\Re\Phi_{34,y}(x_0,x_0)\). These are the real parts
of the original opposite momenta, so \(p_3+p_4=0\).
At the actual internal critical heights, (12) and stationarity give
\[
 \boxed{\quad
 \sup_u\Re F(u+ih;x_0+\zeta,x_0+\omega)
 \le M_{34}+p_3\zeta+p_4\omega
                     -\frac\pi8(\zeta^2+\omega^2).
 \quad}
 \tag{16}
\]
Again the indices range over the entire enlarged central box.
The critical point need not be followed as the external variables move.

## 4. The noncentral profiles retain their gaps near the reference

The previous sections concern the main profiles. The complete source
bounds also retain physical tails, lattice corrections and joining
contours. The following argument includes every one of those terms.

Let \(\delta_{34}>0\) be the minimum of the paired theorem's
proved gaps \(19/3750\), \(1/20\), and \(\delta_J\).
Let \(\delta_{\rm cap}>0\) be the minimum of the prepared
theorem's proved gaps \(1/400\), \(1/20\), and its own
\(\delta_J\). No new optimization enters these definitions.
Each is less than \(1/20\).

Every retained boundary coordinate in either profile family has
\(|\Im a|\le.102\), \(|Z|<.7\), and \(|X|=\rho<5/8\).
These statements also hold throughout a whole real Fourier period.
From (2),
\[
 \partial_x\Re\ell_a(x)
       =-2\pi\Im a+\log|1-Z|-\log|1-X|.
 \tag{17}
\]
The ratio inside the last logarithmic difference lies between
\(12/65\) and \(68/15\), both between \(e^{-2}\) and
\(e^2\). Also \(2\pi(.102)<1\). Hence
\[
                 |\partial_x\Re\ell_a(x)|<3.
 \tag{18}
\]
The same bound holds for \(|p_{\rm cap}|,|p_3|,|p_4|\).
The phases are stationary in their internal variables, so their
external derivatives are the derivatives of their boundary incidences.

Define the two positive radii
\[
 r_{\rm cap}=\min\{1/1000,\delta_{\rm cap}/100\},\qquad
 r_{34}=\min\{1/1000,\delta_{34}/100\}.
 \tag{19}
\]
By (1), all real shifts of size at most \(1/1000\) stay inside
(5). A nonmain paired profile is at most
\[
 M_{34}-\delta_{34}+3(|\zeta|+|\omega|).
\]
Subtract the right side of (16). If both shifts have modulus at
most \(r_{34}\), the result is bounded by
\[
 -\delta_{34}+6(|\zeta|+|\omega|)
             +\frac\pi8(\zeta^2+\omega^2)<-\delta_{34}/2.
 \tag{20}
\]
Indeed the linear cost is at most \(12\delta_{34}/100\)
and the quadratic cost is less than \(\delta_{34}/100\).
The same calculation for the cap gives a gap greater than
\(\delta_{\rm cap}/2\) below (10) for every nonmain profile
when \(|\theta|\le r_{\rm cap}\).

Taking the maxima that define the original transported bounds proves
\[
 \begin{split}
 \mathcal W(\theta)&\le p_{\rm cap}\theta-\frac\pi2\theta^2,
                                      &&|\theta|\le r_{\rm cap},\\
 \mathcal B_{\rm coh}(\zeta,\omega)
 &\le M_{34}+p_3\zeta+p_4\omega
                         -\frac\pi8(\zeta^2+\omega^2),
                                      &&|\zeta|,|\omega|\le r_{34}.
 \end{split}
 \tag{21}
\]
Here \(\mathcal W\) and \(\mathcal B_{\rm coh}\) are
the full profile maxima of the two transport theorems, including all
noncentral terms. Their periodized versions agree with them on these
intervals. Replacing the kernel bound locally by its proved actual
phase only decreases it, so (21) also holds for that replacement.
No value of a finite quantum sum has been used to define these rates.

## 5. Consequence and remaining scope

On the diagonal, the momentum cancellation gives the particularly
simple bound
\[
 \mathcal B_{\rm coh}(\theta,\theta)
           \le M_{34}-\frac\pi4\theta^2
                    \qquad (|\theta|\le r_{34}).
 \tag{22}
\]
Thus this coherent bound has genuine quadratic decrease on an
explicit interval, whereas the original absolute physical-row bound
has a strict excess there. A scalar weight is not being used to
remove a diagonal excess: the internal sum has already been treated
coherently in the complete kernel theorem.

More generally, with the linear weight \(W_{\rm lin}(t)=-p_3t\),
(21) gives
\[
 W_{\rm lin}(\zeta)+\mathcal B_{\rm coh}(\zeta,\omega)
               -M_{34}-W_{\rm lin}(\omega)
       \le-\frac\pi8(\zeta^2+\omega^2).
 \tag{23}
\]
This is a local weighted rate inequality. The linear weight has
not been identified with the actual prepared phase or extended to
an invariant full-period source norm. The radii (19) are expressed
in the already proved contour gaps and are not claimed to contain
the seam center of an arbitrary actual attachment. Consequently
neither the whole-period Schur estimate nor the compensated endpoint
inequalities follow from (21)--(23).
