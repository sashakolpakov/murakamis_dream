# A calibrated nonzero observation of the full homogeneous remainder

Research deduction, 7 November 2026. The exact Casoratian and the
complete second-period packet give a nonzero two-point observation
of the original homogeneous remainder. Its action is exactly the
selected left conditional action, including the additive constant.
The calibration follows through explicit original-strip paths to
a real anchor; no exponentiated derivative is used to discard a
logarithmic lift.

This proves a packet for the specified observation, not for the
homogeneous remainder alone. The known particular current is retained
when the observation is written in terms of the complete finite
conditional source. No numerical evaluation is used.

## 1. Two critical actions on their original strips

Fix \(y=x_0\) and
\[
       a\in[267/1000,433/1000]+i[-9/125,17/250].
 \tag{1}
\]
Let \(s_1\) be the selected original left root from
[the left zero-mode theorem](research_mixed_three_fourier_conditional_left_zero_mode.md),
and let \(z_2=s_2-1\) be the root of the complete
[second-period packet](research_mixed_three_fourier_conditional_second_period_packet.md).
Their phases are
\[
 \begin{split}
 \Phi_1(a,y)
   &=g(s_1+a)+g(s_1+y)-2g(s_1)-g(a)-g(y)+2\pi ias_1,\\
 \Psi_2(a,y)
   &=g(z_2+a)+g(z_2+y)-2g(z_2+1)-g(a)-g(y)
                                      +2\pi i(a-1)z_2 .
 \end{split}
 \tag{2}
\]
Both stationary equations have the original zero logarithmic lift.
Set \(x=\Re a,\ \xi=\Re y,\ \sigma=\Re s_1,\ \tau=\Re z_2\).
The proved strip geometry is
\[
 \begin{gathered}
 0<x,\xi<1/2,\quad 1/4<\sigma<1/2,\quad x+\sigma>1/2,\\
 -\min(x,\xi)<\tau<0,\qquad
             0<x+\tau,\xi+\tau<1/2 .
 \end{gathered}
 \tag{3}
\]
All primitives in (2) are the original functions on \(0<\Re z<1\).
Define the Casoratian action
\[
               \Omega(a,y)=\pi i(a-a^2)-g(a)-g(y).
 \tag{4}
\]

**Theorem 1.** On a fixed neighborhood of the compact family (1),
\[
                          \boxed{\Phi_1+\Psi_2=\Omega.}
 \tag{5}
\]

## 2. The derivative lifts are zero, not merely integral

Put \(X=e^{-2\pi ia},\ W=e^{-2\pi iy}\), and
\[
             d_1=e^{2\pi is_1},\qquad d_2=e^{2\pi iz_2}.
 \]
They are the two roots of
\[
                    (X-1)d^2+(W-X)d+X(1-W)=0 .
 \tag{6}
\]
The stationary chain rule gives for either critical phase
\[
 \lambda_{a,i}:=e^{\partial_a\Phi_i}
       =\frac{d_i-X}{1-X},\qquad
 \lambda_{y,i}:=e^{\partial_y\Phi_i}
       =\frac{1-W/d_i}{1-W},
 \tag{7}
\]
where \(\Phi_2\) denotes \(\Psi_2\) in this equation.
The extra integer in the chirp of \(\Psi_2\) has no effect
on these exponentials. Vieta's formulas give exactly
\[
             \lambda_{a,1}\lambda_{a,2}=\frac{X}{X-1},
       \qquad \lambda_{y,1}\lambda_{y,2}=\frac1{1-W}.
 \tag{8}
\]
These are the exponentials of the two derivatives of (4).

Let \(\Delta=\Phi_1+\Psi_2-\Omega\). Thus each partial
derivative of \(\Delta\) takes values in \(2\pi i\mathbb Z\).
We identify those integers using only the original strip arguments.
For \(0<r<1/2\),
\[
       0<\Im g'(r+iH)<\pi(1-2r),
 \]
whereas for \(1/2<r<1\),
\[
       \pi(1-2r)<\Im g'(r+iH)<0
 \tag{9}
\]
at every finite real height \(H\). Write \(A(w)=\Im g'(w)\).
From (2)--(4),
\[
 \Im\Delta_a
   =A(s_1+a)+A(z_2+a)-A(a)
                          +2\pi(\sigma+\tau)-\pi(1-2x).
 \tag{10}
\]
Applying (9) on the strips in (3) proves
\[
              -\pi+2\pi(x+\tau)<\Im\Delta_a<2\pi\sigma,
 \tag{11}
\]
an interval strictly contained in \((-\pi,\pi)\).
Therefore \(\Delta_a=0\).

Similarly
\[
              \Im\Delta_y=A(s_1+y)+A(z_2+y)-A(y).
 \tag{12}
\]
If \(\sigma+\xi\le1/2\), its lower bound is
\(-\pi(1-2\xi)>-\pi\); otherwise its lower bound is
\(-2\pi\sigma>-\pi\). Its upper bound is strictly below
\(2\pi\) in either case, because each positive contribution
has argument below \(\pi\). Hence
\[
                           -\pi<\Im\Delta_y<2\pi
 \tag{13}
\]
and \(\Delta_y=0\). These conclusions hold on every connected
original-strip chart satisfying (3). They do not yet fix the
constant value of \(\Delta\).

## 3. An explicit path fixes the absolute constant

For each point of (1), connect its two critical phases to the
anchor \(a=y=1/4\) as follows.

First move the incoming height to zero at fixed incoming real
part and fixed \(y=x_0\). This stays in the original rectangle,
where (3) and both original lifts are already proved.

Next hold the now real \(a=x\) fixed and reduce \(\Im y\)
to zero, keeping \(\Re y=\xi\) fixed. In cotangent coordinates
write
\[
              P=p=\cot(\pi x),\qquad Q=q-ib .
 \]
Throughout this segment,
\[
       0<p<9/10,\qquad q\ge127/100,\qquad 0\le b<73/100 .
 \tag{14}
\]
Indeed \(q=\sin(2\pi\xi)/[\cosh(2\pi\Im y)-\cos(2\pi\xi)]\)
increases as the output height decreases.
The function \(b=\sinh T/(\cosh T-\cos(2\pi\xi))\) increases
with \(T\) on the required interval: its derivative has
numerator \(1-\cos(2\pi\xi)\cosh T>0\), using the inherited
bounds \(\cos(2\pi\xi)<41/100\) and \(\cosh T<563/500\).

The [cotangent criterion](research_mixed_three_conditional_root_criterion.md)
stays strictly positive. For example its convex tangent
test in [the actual-input proof](research_mixed_three_conditional_actual_input_subdomain.md)
is satisfied by
\[
                 0+\frac{45}{127}p<\frac{17}{25}.
 \tag{15}
\]
Thus the selected root stays simple in \(\Re S_1>0\),
\(|\Im S_1|<1\).

It also stays below the cotangent real axis. For \(b>0\),
if \(S_1=u+iv\) had \(v\ge0\), the imaginary equation would
give \(u\ge(q-p)/b\) and \(0\le v<b/2\). Its real equation
would then be greater than
\[
 \frac{(q-p)^2}{b^2}+\frac{q^2-p^2}{b}+b-1
 >\frac{(37/100)^2}{(73/100)^2}
       +\frac{8029/10000}{73/100}-1>0,
 \tag{16}
\]
a contradiction. At \(b=0\) the imaginary equation directly
has \(\Im S_1<0\), since \(q>p\).
The divided-root identity of the action-height note now gives
\(|S_1|<1\), also at \(b=0\). Thus \(\sigma>1/4\).
The other root has \(|S_2|>q>1\), hence \(\Re s_2>3/4\).
The incoming shifted wall is therefore passed.
For the outgoing wall,
\[
                   \cot\pi(s_2+y)=Q+\frac{Q^2+1}{p+S_1}.
 \tag{17}
\]
Writing \(S_1=u-iv\), the real numerator of the fraction
in (17) is
\[
              (q^2-b^2+1)(p+u)+2qb\,v>0.
 \tag{18}
\]
Here \(q^2-b^2+1>0\) follows already from (14).
Since \(\Re(s_2+y)\in(3/4,3/2)\), (17) places it above
one. This proves all of (3) along the second segment.

Finally both cotangents are real. Interpolate \(p\) to one
and \(q\) to one, keeping \(0<p\le1\le q\) and \(p<q\)
until the final anchor. The root criterion is now
\(p^2+q^2>0\). Its selected root has nonpositive imaginary
part and modulus less than one. The other root has modulus
greater than one. Equation (17), now with \(b=0\), again
places the outgoing shift above its wall. Thus all phase
arguments remain in their original regular strips, including
at the endpoint. The strict strips have neighborhoods along
each compact path, so the zero partial derivatives from
Section 2 imply constancy of \(\Delta\) all the way to
the anchor.

At \(a=y=1/4\), the roots are
\[
                    s_1=3/8,\qquad z_2=-1/8 .
 \tag{19}
\]
The imaginary parts of \(\Phi_1,\Psi_2,\Omega\) are all
zero, using
\(\Im g(t)=\pi(t-t^2)/2\) on the real unit interval.
Put \(J(t)=\Re g(t)\). Reflection and the sine duplication
identity give
\[
 J(1-t)=-J(t),\qquad
               J(1/8)-J(3/8)=\frac12J(1/4).
 \tag{20}
\]
The latter follows by integrating
\(\log(2\sin\pi t)+\log(2\cos\pi t)=\log(2\sin2\pi t)\)
with its original zero integration constants.
Consequently
\[
 \Re(\Phi_1+\Psi_2)
    =4[J(1/8)-J(3/8)]-4J(1/4)
    =-2J(1/4)=\Re\Omega.
 \tag{21}
\]
This proves \(\Delta=0\) at the anchor and hence (5),
with its full absolute constant on the actual family.
Holomorphy extends it to a common neighborhood.

## 4. The actual two-point observation has the left-action packet

Let \(H_N=F_N^{\rm hom}\), \(Z_N=\mathcal I_{2,N}\),
\(\delta=1/N\), and \(r=e^{-2\pi i/N}\). The exact
[Casoratian theorem](research_mixed_three_fourier_conditional_homogeneous_period.md)
gives, for all sufficiently large \(N\),
\[
 \begin{split}
 \mathcal W_N(a,y)
   &=H_N(a,y)Z_N(a+\delta,y)-H_N(a+\delta,y)Z_N(a,y)\\
   &=\frac rN\,
       \frac{e^{\pi i\{N(a-a^2)-3a\}}E_N(a)E_N(y)}
                                      {(1-rX)^2}.
 \end{split}
 \tag{22}
\]
It is nonzero throughout the admitted state domain. Its packet is
\[
 \mathcal W_N=N^{-2}\mathcal C_W(a,y)e^{N\Omega(a,y)}
                                      (1+O(N^{-1})),
 \qquad
 \mathcal C_W=
 \frac{e^{-3\pi ia}}{(1-X)^2\mathfrak a(a)\mathfrak a(y)}.
 \tag{23}
\]
The complete second-period packet is
\[
 Z_N=N^{-3/2}\mathcal C_Z(a,y)e^{N\Psi_2(a,y)}
                                      (1+O(N^{-1})),
 \quad
 \mathcal C_Z=
 i\sqrt{2\pi}\,
   \frac{\mathcal A_2(z_2;a,y)}{\sqrt{\Psi_{ss}(z_2;a,y)}}.
 \tag{24}
\]
Both coefficients are nonzero, and the normalized errors have
all fixed holomorphic jets on smaller neighborhoods.

Define the exact holomorphic coefficient and observation
\[
 R_N(a,y)=\frac{Z_N(a+\delta,y)}{Z_N(a,y)},\qquad
 \mathcal O_N(a,y)=H_N(a+\delta,y)-R_N(a,y)H_N(a,y).
 \tag{25}
\]
The packet (24) makes this division legitimate on a fixed
neighborhood for every sufficiently large level. Equations
(22)--(25) give the literal identity
\[
                        \mathcal O_N=-\frac{\mathcal W_N}{Z_N}.
 \tag{26}
\]
Using (5), we obtain the nonzero packet
\[
 \boxed{\quad
 \mathcal O_N
     =N^{-1/2}\mathcal C_O(a,y)e^{N\Phi_1(a,y)}
                              (1+O(N^{-1})),\qquad
                  \mathcal C_O=-\mathcal C_W/\mathcal C_Z\ne0 .
 \quad}
 \tag{27}
\]
Every fixed derivative of its normalized holomorphic error is
\(O(N^{-1})\) on smaller neighborhoods. Both parities retain
the original finite interpolation and all scalars.

To state (25) directly in original finite-source variables, keep
the entire particular contribution:
\[
 \begin{split}
 \mathcal O_N={}&C_{0,N}(rX,W)-R_N C_{0,N}(X,W)\\
 &-\{F_N^{\rm part}(a+\delta,y)-R_NF_N^{\rm part}(a,y)\}.
 \end{split}
 \tag{28}
\]
Thus no endpoint forcing or finite periodic zero was discarded.
Restoring the outside twice-crossed scalar gives the specified
observation of its source
\[
 \frac{\kappa^{-2}e^{\pi i(N-1)y}}N\mathcal O_N
   =\kappa^{-2}N^{-3/2}e^{-\pi iy}\mathcal C_O\,
          e^{N\{\Phi_1+\pi iy\}}(1+O(N^{-1})).
 \tag{29}
\]

**Corollary 2 (the full two-point state cannot vanish at the left rate).**
On every smaller compact neighborhood of (1), there are constants
\(c>0\) and \(N_0\), independent of the point and of the parity, such that
\[
 \boxed{\quad
 \max\{|H_N(a,y)|,\ |H_N(a+1/N,y)|\}
       \ge cN^{-1/2}e^{N\Re\Phi_1(a,y)}
       \qquad(N\ge N_0).
 \quad}
 \tag{30}
\]

Indeed the differentiated uniform packet (24), with its nonzero
coefficient on a slightly larger neighborhood, gives
\[
 R_N(a,y)=e^{\partial_a\Psi_2(a,y)}(1+O(N^{-1})).
 \tag{31}
\]
To see the uniformity, write its normalized error as \(e_N=O(N^{-1})\).
Its derivative is also \(O(N^{-1})\), so
\(e_N(a+1/N,y)-e_N(a,y)=O(N^{-2})\); the coefficient ratio
is \(1+O(N^{-1})\), and Taylor's formula gives
\(N[\Psi_2(a+1/N,y)-\Psi_2(a,y)]
=\partial_a\Psi_2(a,y)+O(N^{-1})\).
Thus \(|R_N|\le C_R\) uniformly. The nonzero packet (27) and
\[
 |\mathcal O_N|
 \le (1+C_R)\max\{|H_N(a,y)|,\ |H_N(a+1/N,y)|\}
\]
prove (30). This is a lower bound for the actual neighboring
state vector; it does not specify which entry supplies it.

The coefficient \(R_N\) is defined by the original second period;
it is not asserted to be an arbitrary prescribed closing row or
a fixed crossing word. Equation (27) proves a nonzero observed
component at the original left action. It does not bound the
component of \(H_N\) annihilated by (25), or establish a leading
packet for \(H_N\) itself. A full twice-crossed asymptotic and
subsequent arbitrary short-source propagation still require that
remaining connection estimate.
