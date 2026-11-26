# The first cap through the upper target interval

Research deduction, 7 November 2026. The original first-cap source
envelope and its joint horizontal curvature extend to real targets
through \(1/2\). This gives a main-current Dirichlet inequality
at the original height on the enlarged interval. It does not
give a sign on the height taper. A separate local statement below
shows why a standalone cap supporting plane cannot control every
attenuated height, even when the full complex tangent is retained.
No numerical or source evaluation is used.

## 1. The enlarged regular product and its exact curvature

Use the original cap and phase
\[
 \begin{split}
 U_{\alpha,N}(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})(rX;r)_i}{(r;r)_i^{1+\alpha}},
       \qquad X=e^{-2\pi iz},\quad r=e^{-2\pi i/N},\\
 \Psi_\alpha(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),\\
 \Xi_\alpha(e,z)&=\Psi_\alpha(e,z)-\frac\alpha2g(z),
       \qquad \alpha\in\{0,1\}.
 \end{split}
 \tag{1}
\]
All normalizations and logarithms are those in the
[original cap contour theorem](research_mixed_cap_outer_contour_reduction.md).
Set
\[
 E_c=[.27,.49]+i[-.055,.04],\qquad
 P^+=[.22,.5],\qquad Z^+=P^++i[-.108,.021].
 \tag{2}
\]
In particular \(.49\le\Re(e+z)\le.99\), so no primitive
argument reaches a real-period wall.

**Lemma 1.** Throughout \(E_c\times Z^+\),
\[
       -\Re\Psi_\alpha''\succ\frac\pi{200}I_2,
       \qquad -\Re\Xi_\alpha''\succ\frac\pi{200}I_2 .
 \tag{3}
\]
Here these are real symmetric matrices of real parts of the
holomorphic Hessian entries.

*Proof.* On \(\Re z\le.45\), this is Lemma 1 of the
[full cap phase theorem](research_mixed_first_cap_plateau_phase.md).
On the additional strip \(.45\le\Re z\le.5\), put
\[
 s=-\Re S''(e)/\pi,\quad p=\Re\cot\pi z,\quad
 q=\Re\cot\pi e,\quad d=-\Re\cot\pi(e+z).
 \tag{4}
\]
The same original endpoint proof supplies \(s>1/43\).
We have \(p\ge0\), \(q>0\), and
\(.72\le\Re(e+z)\le.99\), \(|\Im(e+z)|\le.163\).
Consequently
\[
 d=\frac{-\sin(2\pi\Re(e+z))}
          {\cosh(2\pi\Im(e+z))-\cos(2\pi\Re(e+z))}
       >\frac{3}{130}.
 \tag{5}
\]
Indeed the numerator is at least \(\sin(.02\pi)>3/50\).
Also \(.326\pi<41/40\), and the elementary positive-series
bound gives
\[
 \cosh(.326\pi)
 <1+\frac{(41/40)^2}{2}
       +\frac{(41/40)^4}{24(1-(41/40)^2/30)}
 <\frac85.
 \tag{6}
\]
The denominator in (5) is thus less than \(13/5\).

The bare negative Hessian, divided by \(\pi\), is
\[
 \begin{pmatrix}s+\alpha q+d&d\\d&p+d\end{pmatrix}
 \succeq
 \begin{pmatrix}1/43+3/130&3/130\\3/130&3/130\end{pmatrix}.
 \tag{7}
\]
The determinant divided by the trace of the last matrix is
\[
 \frac{(1/43)(3/130)}{1/43+6/130}
                  =\frac3{388}>\frac1{200}.
 \tag{8}
\]
For a positive two-by-two matrix this is a lower bound for its
least eigenvalue. The allocated phase adds the nonnegative
diagonal entry \(\alpha p/2\). This proves (3), including
the endpoint \(\Re z=.5\), where \(p=0\). \(\square\)

## 2. The entire finite cap has the same envelope on \(P^+\)

Use the five profiles \(A_{\alpha,0},A_{\alpha,L},
A_{\alpha,R},A_{\alpha,-},A_{\alpha,+}\) in equation (5) of
the [boundary-window color envelope](research_mixed_boundary_window_real_color_envelopes.md),
with the same private main height \(h_e\), real cuts \(.27,.49\),
alias heights \(-.055,.04\), and penalties \(.11\pi,.08\pi\).
Let \(A_\alpha(z;h_e)\) be their maximum. Only the outgoing
real interval is enlarged here. Keep the original height ranges
\[
 \begin{cases}
 -.072\le h\le .021,&\alpha=0,\\
 -.108\le h\le .014,&\alpha=1,
 \end{cases}
 \qquad z=y+ih,\quad y\in P^+ .
 \tag{9}
\]

**Theorem 2.** There is \(c>0\) such that for every
\(\eta>0\),
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\eta N^{a_\eta}
 \left[
 e^{N\{A_\alpha(z;h_e)-c(1-\cos\theta)+\eta\}}
        +e^{N(3/4+\eta)}
 \right].
 \tag{10}
\]
Uniformity, both parities and fixed ordinary-color derivatives
have the same scope as the cited envelope theorem. In particular
all retained currents, physical tails, revived Newton rows and
vertical joins are present. The theorem concerns the bare literal
cap; a retained Fourier weight must still use its own exact bound.

*Proof.* The exact interpolant is unchanged:
\[
 D_N(e)^{-1}C_N(e,w)
 \frac{\widehat P_N(N(e+z))}
      {\widehat P_N(Nz)\widehat P_N(Ne)^\alpha}.
 \tag{11}
\]
The whole coherent coefficient still lies in \(E_c\), where
the [real-color coefficient theorem](research_mixed_endpoint_real_color_decay.md)
supplies \(\Re S(e)-c_E(1-\cos\theta)\). The arguments
of the other factors in (11) are regular by (2).
Lemma 1 supplies the private vertical convexity used for every
zero-mode join and each sign-half vertical alias. Thus precisely
the five old current profiles control the retained contour on the
larger outgoing interval, with the angular loss unchanged.

It remains to check that extending \(y\) does not omit a physical
tail. Its original compact-row rate is
\[
 R_\alpha(t,z)=\Re S(t)+2\pi h_+t
   +\int_0^t\log|1-e^{-2\pi|h|-2\pi i(y+x)}|\,dx
                                             -\alpha J(t).
 \tag{12}
\]
For \(0<t\le.27\), now
\(.22\le y+t\le.77\). Throughout that interval the cosine
of twice the angle is less than \(1/5\): its endpoint bounds
are \(\sin(.06\pi)<1/5\) and
\(\sin(.04\pi)<1/5\). The smoothed radius exceeds \(1/2\).
The lower-tail derivative proof therefore remains unchanged.

For the type-four upper tail and the bridge \([.49,.5]\),
the numerator bound \(1+e^{.028\pi}<9/4\) is independent
of \(y\); hence the proof in the cited envelope applies verbatim.
For type three, the inequality
\[
 \sin(\pi t)|\sin(\pi(t+y))|\le\cos(.22\pi),
                     \qquad t\ge.5,\quad y\in[.22,.5],
 \tag{13}
\]
still holds. Before \(t+y=1\) the product decreases from
\(\cos\pi y\); after that wall its absolute maximum is
\((1-\cos\pi y)/2\le1/2\). Thus the original estimate
in equation (18) of the full cap phase theorem is unchanged.
On the bridge, \(t+y\in[.71,1]\); the old bound
\(|\sin\pi(t+y)|\le\sin(.29\pi)\) still applies.
These compact physical bounds retain their positive angular
loss from the physical-index coefficient theorem. At numerator
zeros, the integrated logarithm is continuous and the original
finite product estimates are zero safe.

Finally, the true index-end estimates also survive. The lower
endpoint uses only the radius bound and lower-half Newton entropy.
For \(i/N\ge.99\), the denominator angles in the exact identity
\[
 (rX;r)_i=\frac{1-X^N}{\prod_{j=i+1}^{N}(1-r^jX)}
 \tag{14}
\]
now lie in \([.21,.5]\). Minimizing their moduli over the
radius still gives the old lower bound \(19/20\): when the
cosine is positive use \(\sin(.42\pi)>19/20\), and otherwise
use one. The same ceiling
\(3/5+2\pi h_++\log(40/19)/100<3/4\) follows.
Above the Newton half point this uses only \(V_\theta\le0\),
not the stronger complete-color entropy. The unchanged finite
row and current count proves (10), with one total tolerance.
\(\square\)

The angular-surplus implication also survives: whenever a proved
bound \(A_\alpha\ge3/4+\delta\) holds on a chosen subset of
(9), (10) has the single exponent
\(A_\alpha-\min(c,\delta/2)(1-\cos\theta)+\eta\).
No such surplus on every enlarged target is asserted.

## 3. The main Dirichlet bound at the original height

Fix an actual cap reference \(e_*=b+ih_*\), \(z_*=a+ic\),
and its allocated action and marginal
\[
 L_\alpha(z)=\mathcal T_\alpha(z,-2)-\frac\alpha2g(z),
                         p=L_\alpha'(z_*).
 \tag{15}
\]
The private stationary equation is the original one, and
\(\Xi_\alpha(e_*,z_*)=L_\alpha(z_*)\).
For every \(x\in[.27,.49]\) and \(y\in P^+\), the
fixed-height segment from the actual reference remains in (2).
Integrating (3) twice gives
\[
 \begin{split}
 \Re\Xi_\alpha(x+ih_*,y+ic)
 \le \Re L_\alpha(z_*)+\Re p\,(y-a)
             -\frac\pi{400}\bigl((x-b)^2+(y-a)^2\bigr).
 \end{split}
 \tag{16}
\]
The analogous bare inequality uses \(\Psi_\alpha\) and
\(\mathcal T_\alpha'\). Thus the original-height main current
does have its Dirichlet comparison through \(y=.5\), without
introducing a moving saddle there.

Equation (16) alone does not pay the four cut/alias profiles in
(10) at the newly admitted real targets. Nor may it be evaluated
at a different outgoing height as though the segment were
horizontal. These are distinct remaining source comparisons.

## 4. A literal local obstruction to a standalone reset bound

The completed [cap theorem](research_mixed_first_cap_plateau_completion.md),
equation (4), supplies the original nonzero local packet near
every actual reference,
\[
 U_{\alpha,N}(-2,e^{-2\pi iz})
   =N^{-1-\alpha/2}\mathcal B_\alpha(z,-2)
          e^{N\mathcal T_\alpha(z,-2)}(1+O(N^{-1})),
                    \qquad \mathcal B_\alpha\ne0.
 \tag{17}
\]
This statement concerns a sufficiently small fixed neighborhood
of the actual reference only. In that neighborhood the original
holomorphic private branch \(e(z)\) remains in \(E_c\).
For either the bare or allocated phase, let \(H\) be its
complex symmetric Hessian and \(v=(e'(z),1)^T\).
Differentiating private stationarity gives
\[
       Hv=(0,T''(z))^T,\qquad
       -\Re T''(z)=v^*(-\Re H)v>\frac\pi{200}.
 \tag{18}
\]
Here \(T=\mathcal T_\alpha\) or \(L_\alpha\), respectively.
The second equality uses the Hermitian part of a complex
symmetric Hessian; it involves no bilinear modulus substitution.

For any sufficiently small real \(\tau\) such that the
vertical segment stays in that neighborhood, put
\[
 D_T(\tau)=
 \Re\{T(z_*+i\tau)-T(z_*)-T'(z_*)i\tau\}.
 \tag{19}
\]
Then \(D_T(0)=D_T'(0)=0\) and
\(D_T''(\tau)=-\Re T''(z_*+i\tau)>\pi/200\). Hence
\[
                         D_T(\tau)>\frac\pi{400}\tau^2
                                    \quad(\tau\ne0).
 \tag{20}
\]
For the bare source, (17) proves that its modulus at any such
fixed nonzero \(\tau\) exceeds every polynomial multiple of
the original affine-plane exponential. For the allocated version,
the same conclusion holds on the original local unselected
Fourier branch; at type four choose the segment at negative
height so the nonzero local \(d_N\) packet supplies exactly
\(-g/2\). This is a finite-source consequence of the known
nonzero packet, not just positivity of a loose upper envelope.

In particular an arbitrarily small attenuation of a nonzero
negative original height toward zero, while holding its real
coordinate at \(a\), cannot obey an independent cap sign
against the original complex tangent. The statement includes the
imaginary tangent in (19); dropping it is not its cause.

This does not contradict a sign for the
[contracted boundary functional](research_mixed_contracted_finite_boundary_windows.md).
A physical attenuation is caused by neighboring target states;
their literal factors, tangent cancellation and residual energy
are absent from this standalone test. They may pay (20).
The safe bulk proof already keeps such coupled energy. What
remains at a physical boundary is to control its actual source
profiles together with that neighboring energy. Lemma 1 and
Theorem 2 remove a domain and real-color obstacle on
\([.45,.5]\), but assert no global taper monotonicity, boundary
sign, or whole-source asymptotic.
