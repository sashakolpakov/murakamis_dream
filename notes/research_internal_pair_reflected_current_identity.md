# Reflected middle currents and their original moving-wall residues

Research proof, updated 4 November 2026. Frozen manuscripts are unchanged.

Reflecting both negative factorial arguments reorganizes the exact
middle integrand into terms with fewer wire or trace poles. The
reorganization is legitimate, but its pieces acquire moving poles
when extended out of that chamber. Their residues are nonzero and
recover the original value-support rows. Thus the pieces without
a wire denominator cannot simply be discarded by a wire Cauchy
argument.

The later sections estimate the original integrand without
discarding those terms. Sections 13–14 give coupled angular
contours and the right vertical wire side for every fixed
positive pair of powers at least seven. Together with the left
contour and endpoint estimates, these supply the
[full two-boundary source theorem](research_internal_pair_combined_contour_reduction.md#7-the-full-source-for-every-fixed-pair-of-powers-at-least-seven).

## 1. Exact denominator cancellation, with the common scalar

Put
\[
 \begin{gathered}
 q_x=e^{-2\pi iNx},\quad q_t=e^{-iNt},\quad q_r=e^{-iNr},
 \qquad D_t=1-\eta q_t,\quad D_r=1-\eta q_r,\\
 w_t=\frac12-x-\frac{t}{2\pi},\qquad
 w_r=\frac12-x-\frac{r}{2\pi},\qquad \eta=(-1)^{N-1}.
 \end{gathered}
 \tag{1}
\]
The exact reciprocal reflection is
\[
 \frac1{G_N(Nw_t-1/2)}
 =E_N(x,t)(1-\eta q_xq_t),\qquad
 E_N(x,t)=\frac{e^{-i\pi Nw_t}}N G_N(-Nw_t-1/2).
 \tag{2}
\]
It is a meromorphic identity; its product is regular wherever
the original reciprocal factorial is regular.

For the original interpolation define
\[
 C_N(x,t)=
 \frac{G_N(-Nw_t-1/2)}
 {G_N(N(1/2-x+t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{3}
\]
Then \(B_N(x,t)=C_N(x,t)e^{-i\pi Nw_t}
(1-\eta q_xq_t)\), and likewise for \(r\).
Using the literal one-cell wire kernel
\(1/(1-e^{2\pi iNx})=-q_x/(1-q_x)\), one obtains
\[
 \begin{split}
 &\frac{B_N(x,t)B_N(x,r)}
                 {1-e^{2\pi iNx}}
      \frac{q_tq_r}{D_t^2D_r^2}\\
 &\quad=\eta C_N(x,t)C_N(x,r)e^{-iN(t+r)/2}
 \left\{
 \frac{1-q_x}{D_t^2D_r^2}
 +\frac{q_x}{D_tD_r^2}
 +\frac{q_x}{D_t^2D_r}
 +\frac{q_x^2}{(1-q_x)D_tD_r}
 \right\}.
 \end{split}
 \tag{4}
\]
Indeed
\(1-\eta q_xq_t=(1-q_x)+q_xD_t\).
The common reflection exponential contributes
\((-1)^Nq_x^{-1}e^{iN(t+r)/2}\); together with the original
wire and trace kernels this gives exactly the scalar and
half-charge exponential in (4).
The sine factors and original crossing Gaussians multiply
both sides unchanged.

In the chamber \(\Re w_t,\Re w_r<0\), the reflected numerator
factorials in (3) have positive scaled real part. Formula (4)
is consequently a useful exact grouping there. Extending an
individual term across a chamber wall requires the residues
described next.

## 2. The artificial poles recover actual value-support rows

Write \(S_j=\prod_{\ell=1}^j2\sin(\pi\ell/N)\), \(S_0=1\).
The canonical shift relation and \(G_N(0)=1\) give, for
\(1\le k\le N\),
\[
 \operatorname*{Res}_{z=-k}G_N(z)
                =\frac{(-1)^{k-1}N}{2\pi S_{k-1}} .
 \tag{5}
\]
For \(k=1\), use
\(G_N(z)=G_N(z+1)/(2\sin(\pi(z+1)/N))\).
The remaining cases follow by the next \(k-1\) shifts;
their nonzero sine product is \((-1)^{k-1}S_{k-1}\).

For fixed \(x\), the factor \(E_N(x,t)\) in (2) therefore has
simple poles at
\[
 t_k(x)=\pi-2\pi x-\frac{(2k-1)\pi}{N},
 \qquad w_t=\frac{k-1/2}{N},
 \qquad
 \operatorname*{Res}_{t=t_k(x)}E_N(x,t)
                      =-\frac{i}{N S_{k-1}} .
 \tag{6}
\]
The sign includes \(d(-Nw_t-1/2)/dt=N/(2\pi)\) and
\(e^{-i\pi(k-1/2)}=i(-1)^k\).
At the same point,
\[
 1-\eta q_xq_t=0,\qquad
 \partial_t(1-\eta q_xq_t)=iN .
 \tag{7}
\]
Thus the product in (2) has the regular value
\[
 \lim_{t\to t_k(x)}
 E_N(x,t)(1-\eta q_xq_t)=\frac1{S_{k-1}},
 \tag{8}
\]
exactly \(1/G_N(k-1)\). The moving poles are artifacts of
splitting the reflection multiplier; the unsplit original
factor has no pole there.

At a genuine low wire sample \(x=j/N\), a moving pole in the
nonnegative physical half-period has
\[
 t_k(j/N)=\tau_a,\qquad
          j\le a=j+k-1\le\lfloor(N-1)/2\rfloor .
 \tag{9}
\]
These are precisely the original value-support rows among the
distinct physical roots, not the below-triangle normal-only
rows \(a<j\). Negative angles are paired by evenness and
exchange the two shifted factorials; no assertion that the
residue of the isolated factor \(E_N\) survives all the other
factors on every duplicated grid row is needed.
For example, when \(0\le j\le a\le\lfloor(N-1)/2\rfloor\),
the remaining factors in (2) and (8) recover
\[
 e_j(c_a)
 =\frac{N}{S_{N-1-a-j}S_{a-j}S_j^2}
 =\frac{S_{a+j}}{S_{a-j}S_j^2}>0 .
 \tag{10}
\]
This is also the direct original Newton product.
At \(j=0\) it equals the exact cap value one.
The meromorphic identity (2) holds on a neighborhood of
each canceled pole, so it retains its full ordinary jets,
not just this value.

Consequently the first three terms of (4), although lacking
the original wire denominator, can have nonzero moving-wall
residues through \(C_N(x,t)C_N(x,r)\).
At a wall, \(D_t=1-q_x^{-1}\), and the two summands of
\((1-q_x)+q_xD_t\) cancel; the complete expression cancels
the artificial residues exactly. At intersections or at
physical wire samples this cancellation must be performed
together with the original trace poles.

This gives a precise restriction on a prospective middle-band
deformation. One may keep the reflected pieces inside their
chamber, or extend them while retaining these wall currents.
There is no justification for treating all such currents as
deleted-edge errors: (9)--(10) identify their direct connection
to the original value sector. The identity makes no global
gap or nonzero closing-coefficient claim.

There is an exact independent description of the support in (9).
The ordinary value interpolant of a crossing times \(e_j\) factors
as \(e_j\) times the crossing interpolant on the remaining distinct
nodes \(a\ge j\). Its Cauchy denominator is therefore
\(\prod_{a\ge j}(z-c_a)\); see the
[source-exact normal-defect regrouping](research_trace_normal_defect_positive_form.md).
These are the same nodes as (9). This identifies the common
support, not an equality between an individual term of (4) and
the whole normal-defect observation: their trace poles must
still be recombined.

## 3. A favorable height direction in the upper reflected chamber

The exact reflected expression also has a useful monotonicity
direction. It concerns the original complete-end phase, including
the crossing and unit-charge terms:
\[
 \mathcal F_n(x,t)
   =b(x,t)+\psi(t,0)+\frac{int^2}{4\pi}-it,\qquad
 \psi_t(t,0)=-\frac1\pi\operatorname{arsinh}\tan(t/2).
 \tag{11}
\]
The branch is continued from the original positive factorial
strip. In particular, when \(w_t\) has negative real part and
positive imaginary part, \(J(w_t)\) is continued through the
upper half-plane. It is not replaced by a fresh principal
logarithm of a final product.

**Proposition 1.** Suppose
\[
 \begin{gathered}
 x=\xi+iY,\qquad 0<\xi<\frac14,\qquad Y>0,\qquad n\ge3,\\
 t=\tau-iH,\qquad
       \pi-2\pi\xi\le\tau<\pi,\qquad H>2\pi Y.
 \end{gathered}
 \tag{12}
\]
Then
\[
 \frac{\partial}{\partial H}\Re\mathcal F_n(x,\tau-iH)
 >
 \frac{(2n-1)\tau}{4\pi}+\frac{\xi}{2}-\frac34
 \ \ge\
 \frac{n-3}{4}+(n-1)\left(\frac14-\xi\right)>0 .
 \tag{13}
\]
The integrated inequality extends to \(H=2\pi Y\) by the
one-sided continuous upper exponent, including the limiting
factorial zero. Thus lowering the trace height within this
chamber strictly decreases its upper phase.

*Proof.* The logarithmic derivative inherited from the strip is
\[
 b_t(x,t)=\frac1{2\pi}
   \{\Log\cos(\pi x+t/2)-\Log\cos(\pi x-t/2)\}.
 \tag{14}
\]
For the numerator, the real part of its cosine argument belongs
to \([\pi/2,\pi)\), and its imaginary part is
\(\pi Y-H/2<0\). Its value is in the closed upper left quadrant,
with argument \(\nu\ge\pi/2\).
For the denominator, the cosine argument has real part
\(\pi\xi-\tau/2\in(-\pi/2,0)\) and positive imaginary part.
Its value is in the first quadrant. Its argument \(\delta\)
satisfies
\[
 0<\delta
 =\arctan\{\tan(\tau/2-\pi\xi)\tanh(\pi Y+H/2)\}
 <\tau/2-\pi\xi .
 \tag{15}
\]
In this chamber \(0<\nu-\delta<\pi\). These arguments agree
with the continued sine-factor logarithms in (14): the
negative shifted argument has been crossed above zero, and
the other shifted argument stays in \(0<\Re w<1\).
There is no logarithmic winding to add. Consequently
\[
                  \Im b_t>\frac14-\frac{\tau}{4\pi}
                                      +\frac{\xi}{2}.
 \tag{16}
\]

For \(0<\tau<\pi\) and \(H>0\), \(\tan(t/2)\) has positive
real part and negative imaginary part. Its selected
\(\operatorname{arsinh}\) likewise has positive real part and
imaginary part in \((-\pi/2,0)\). Hence
\(\Im\psi_t(t,0)>0\).
Since
\(\partial_H\Re\mathcal F_n=\Im(\mathcal F_n)_t\),
the other two derivatives contribute \(n\tau/(2\pi)-1\).
Adding this to (16) proves the first bound in (13).
Substituting the lower bound for \(\tau\) proves the second.

The primitives have continuous real limits as \(H\) decreases
to \(2\pi Y\); at a zero this follows from the local
\(w\log w\) behavior. Integrating (13) first on a closed
subinterval of \(H>2\pi Y\), then taking the lower endpoint
limit, proves the stated one-sided extension. \(\square\)

For example, if \(\xi\le\beta<1/4\) and
\(H_2>H_1\ge2\pi Y\), the phase drop is at least
\[
 \Re\mathcal F_n(x,\tau-iH_2)
 -\Re\mathcal F_n(x,\tau-iH_1)
 \ge
 \left\{\frac{n-3}{4}+(n-1)(1/4-\beta)\right\}(H_2-H_1).
 \tag{17}
\]
It applies separately to either trace variable in the joint
pair phase, without altering the other crossing.

For its use as a finite-source upper estimate, keep the contour
in a compact subset of (12) on which the actual complete-end
low kernel is covered by
\(\Re(-2\cos t)<2\). The
[absolute physical-row theorem](research_last_physical_row_riccati.md)
then supplies its upper phase \(\Re\psi(t,0)\), with only
polynomial losses. The reciprocal-factorial upper bound
retains both terms of (2), including their zeros at the
one-sided boundary. The trace denominator is uniformly
bounded after its original \(e^{-NH}\) penalty is extracted.
Thus (17) is a comparison of the actual available upper
exponents. It is not a ratio bound between finite densities:
the lower-height density can vanish at a reciprocal-factorial
zero. Full outside radicals are still handled after the
original trace by the established source decomposition.

Proposition 1 does not cover \(H<2\pi Y\), \(\xi\ge1/4\),
or the passage between a reflected and a regular trace factor.
Nor does it license discarding the wall residues in Section 2.
It therefore supplies a favorable part of an adapted contour,
not the missing whole middle-band bound.

## 4. Height descent without ordering the wire and trace heights

The same argument gives a useful direction on the lower wire
without any height-order condition. On the upper wire, a power
of at least seven also removes that condition. These statements
concern the original continuous factorial upper exponent; no
separated reflection term or moving-wall residue is discarded.

For \(\sigma\in\{+1,-1\}\), write
\[
 \begin{split}
 x_\sigma&=\xi+\sigma iY,\qquad t=\tau-iH,\\
 E_{n,\sigma}(\xi,\tau,H;Y)
   &=\mathfrak b(x_\sigma,t)+\Re\Psi(t)
                     +\frac{n\tau H}{2\pi}-H,
 \qquad \Psi(t)=\psi(t,0).
 \end{split}
 \tag{18}
\]
Here \(\mathfrak b\) is the continuous upper exponent of the
actual reciprocal factorials, including both reflection terms.
The lower-wire penalty \(-2\pi Y\), when present in the full
pair density, is independent of \(H\) and does not change the
following inequalities.

**Proposition 2.** Suppose
\[
 0<\xi<1/4,\qquad Y>0,\qquad
                 \pi-2\pi\xi\le\tau<\pi.
 \tag{19}
\]
For every real \(n\ge3\), the lower-wire exponent satisfies
\[
 \partial_HE_{n,-}
 >\frac{n-3}{4}+(n-1)(1/4-\xi)>0
                         \qquad(H>0).
 \tag{20}
\]
For every real \(n\ge7\), the upper-wire exponent satisfies,
away from the reflection switch \(H=2\pi Y\),
\[
 \partial_HE_{n,+}
 >\frac{n-7}{4}+n(1/4-\xi)>0.
 \tag{21}
\]
Both give the corresponding integrated inequalities down to
\(H=0\). Equation (21) also integrates across \(H=2\pi Y\)
using the continuous upper exponent there.

*Proof.* Set
\(A=\pi\xi+\tau/2\) and \(B=\pi\xi-\tau/2\).
Then \(\pi/2\le A<\pi\) and \(-\pi/2<B<0\).
The two individual logarithms in (14) are followed with their
original strip continuations. This is essential: the argument
of their quotient must not be reset to \((-\pi,\pi)\).

For the lower wire, the numerator cosine has imaginary
argument \(-\pi Y-H/2<0\). Its argument \(\nu\) therefore
belongs to \([\pi/2,\pi)\). The denominator cosine has
imaginary argument \(-\pi Y+H/2\). Its argument \(\delta\)
satisfies
\[
             \delta<|B|=\tau/2-\pi\xi.
 \tag{22}
\]
Indeed, if that imaginary argument is nonnegative, this is
\(\arctan(\tan|B|\tanh(-\pi Y+H/2))<|B|\).
If it is negative, \(\delta<0\) and the bound is immediate.
The reflected shifted argument has imaginary part
\(Y+H/(2\pi)>0\), fixing its upper continuation. Thus
\[
 \Im b_t(x_-,t)=\frac{\nu-\delta}{2\pi}
                 >\frac14-\frac{\tau}{4\pi}+\frac\xi2.
 \tag{23}
\]
As in Proposition 1, \(\Im\Psi_t>0\), while the crossing
and unit-charge terms contribute \(n\tau/(2\pi)-1\).
Substitute the lower bound on \(\tau\) in (19) to obtain
(20). This calculation never compares \(H\) with \(2\pi Y\).

For the upper wire and \(H>2\pi Y\), Proposition 1 already
gives the stronger bound (20). For \(0<H<2\pi Y\), the
numerator cosine is in the lower left quadrant, with its
continued argument \(\nu\in(-\pi,-\pi/2]\). The denominator
cosine is in the upper right quadrant, with
\(0<\delta<\pi/2\). Now the reflected shifted argument has
negative imaginary part, fixing its lower continuation.
Consequently
\[
 \Im b_t(x_+,t)=\frac{\nu-\delta}{2\pi}>-\frac34,
 \qquad
 \partial_HE_{n,+}>\frac{n\tau}{2\pi}-\frac74
       \ge\frac{n-7}{4}+n(1/4-\xi).
 \tag{24}
\]
The bound from Proposition 1 exceeds the last expression by
\(3/4+\xi\). This proves (21) on both sides of the switch.

On each side the derivative bounds integrate directly. At the
switch the reciprocal-factorial upper exponent is continuous;
its possible limiting sine zero has the integrable
\(w\log w\) primitive. Split an interval at the switch and
pass to the one-sided limits. The same continuity argument
permits the endpoint \(H=0\). \(\square\)

If the starting trace point lies in
\(\Re(-2\cos t)<2\), lowering \(H\) preserves that half-plane
on the range (19). Hence the proved low-complete-kernel
normalization remains applicable along this height descent.
On compact sets with positive trace height, the proposition compares
the available upper exponents for the original low-source densities.
The endpoint \(H=0\) is only an integrated phase limit; the finite
trace denominator has real poles there, so no uniform density bound
at those poles is asserted. It supplies no equality between their
complex integrals and no estimate for the contour connectors
created by a height change. Those connectors and the geometric
contribution still have to be assembled in the exact source.

## 5. When both trace factors are reflected, the real contour has a gap

There is a uniform rate bound for the part with
\(0<\xi\le1/4\) where both trace angles are beyond their
factorial walls. It gives an actual finite-source estimate on
nearby contours of small positive trace height. Connecting those
contours to the rest of the source remains a separate problem.

For real trace angle \(\tau\), let \(V_\tau(\xi)\) be the real
Newton entropy, so
\(\mathfrak b(\xi,\tau)=V_\tau(\xi)\). Use the normalization
\(\Psi(0)=M_\infty=4G/\pi\), with \(G\) Catalan's constant.

**Lemma 3.** If \(0<\xi\le1/4\) and
\(\pi-2\pi\xi\le|\tau|<\pi\), then
\[
 V_\tau(\xi)+\Psi(\tau)
       \le J(2\xi)-2J(\xi)+\Psi(\pi-2\pi\xi)
       \le \frac{M_\infty}{4}+\Psi(\pi/2)<\frac{751}{600}.
 \tag{25}
\]

*Proof.* Both functions are even in \(\tau\). For
\(0<\tau<\pi\), away from the single logarithmic zero,
\[
 \partial_\tau V_\tau(\xi)
  =\frac1{2\pi}\log\left|
       \frac{\cos(\pi\xi+\tau/2)}{\cos(\pi\xi-\tau/2)}\right|<0.
 \tag{26}
\]
Indeed the denominator's squared modulus exceeds the
numerator's by \(\sin(2\pi\xi)\sin\tau>0\).
The derivative has an integrable logarithmic singularity at
the wall, so monotonicity holds across it as well.
Also \(\Psi'(\tau)=-\operatorname{asinh}\tan(\tau/2)/\pi<0\).
At the wall, the factorial primitive gives
\(V_{\pi-2\pi\xi}(\xi)=J(2\xi)-2J(\xi)\).
The latter expression has derivative
\(2\log(2\cos\pi\xi)>0\) for \(\xi\le1/4\).
The function \(\Psi(\pi-2\pi\xi)\) also increases with \(\xi\).
At \(\xi=1/4\), the first expression equals
\(-2J(1/4)=G/\pi=M_\infty/4\).

For clarity, the needed upper estimate at \(\pi/2\) can be
proved with three positive Fourier blocks. The integrated sine
series gives
\[
 \Psi(\pi/2)=\frac{2\sqrt2}{\pi}\sum_{j\ge0} b_j,
 \qquad
 b_j=\frac1{(8j+1)^2}+\frac1{(8j+3)^2}
       -\frac1{(8j+5)^2}-\frac1{(8j+7)^2}.
 \tag{27}
\]
Each block is positive and is at most \(16/(8j+1)^3\),
by integrating the derivative of \(x^{-2}\) over the two
intervals of length four. The decreasing-integrand estimate
therefore gives
\[
 \sum_{j\ge3}b_j
 \le\frac{16}{25^3}+\int_3^\infty\frac{16\,ds}{(8s+1)^3}
 =\frac{41}{15625}.
 \tag{28}
\]
The first three blocks plus this rational tail are less than
\(533/500\). Using \(\sqrt2<99/70\) and \(\pi>333/106\),
\[
 \Psi(\pi/2)<\frac{310739}{323750}<\frac{24}{25}.
 \tag{29}
\]
Finally \(M_\infty<7/6\), so
\(M_\infty/4+\Psi(\pi/2)<7/24+24/25=751/600\).
This proves (25). \(\square\)

The real profile in (25) is the same \(C(\xi)\) used in the
[triangular first-normal estimate](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_pair_triangular_normal_region.md).
That note already bounds the corresponding original two-normal
rows for \(j/N\le1/4\). The point of the next proposition is to
control the actual complex factorial density on nearby contours,
without identifying an arbitrary wall current with those rows.

Fix \(0<\alpha<1/4\) and \(T<\pi\). Consider the compact
real set with empty sections omitted:
\[
 \alpha\le\xi\le1/4,\qquad
 \pi-2\pi\xi\le|\tau|,|\rho|\le T.
 \tag{30}
\]
Both trace signs are allowed independently.
For fixed positive powers \(n,p\ge3\), the original
geometric rate satisfies \(M_{n,p}>63/25\). At zero heights,
the two instances of (25) and all original crossing phases give
\[
 \mathcal E_{n,p}(\xi,\tau,\rho)
     <\frac{751}{300}=\frac{63}{25}-\frac1{60}
     <M_{n,p}-\frac1{60}.
 \tag{31}
\]
Here \(\mathcal E\) is the complete upper exponent from equation
(20) in the [original double-pole density note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md),
including the lower-wire penalty.

**Proposition 4.** There exists \(\varepsilon>0\), depending on
the fixed powers, \(\alpha\), and \(T\), such that this density
has upper bound
\[
 |\mathcal I_N(\xi+iy,\tau-ih_1,\rho-ih_2)|
       \le CN^A\exp\{N(M_{n,p}-1/120)\}
 \tag{32}
\]
on (30), for fixed \(0<h_1,h_2<\varepsilon\) and
\(0<|y|<\varepsilon\). It is uniform when these nonzero
heights range over compact sets. It also holds on half-grid
wire sides \(N\xi\in\mathbb Z+1/2\), with
\(|y|\le\varepsilon\), including \(y=0\).
Fixed selected ordinary normals have the same upper exponent.

*Proof.* The continuous reciprocal-factorial upper exponent
is uniformly continuous on a compact neighborhood of (30),
including its limiting factorial zeros. All other terms of
\(\mathcal E\) are continuous there. Shrink \(\varepsilon\)
so that varying the three heights by at most \(\varepsilon\)
changes the upper exponent by less than \(1/120\).
This preserves (31) with the gap in (32), and with a strict
margin on slightly larger neighborhoods when needed.

The actual low complete kernels have logarithmic phase
\(\Psi\) on this neighborhood: \(T<\pi\) ensures a fixed
margin in \(\Re(-2\cos t)<2\) at zero height. On the real
set, \(\Psi(\tau)\ge\Psi(T)>0\). After further shrinking
\(\varepsilon\), one has
\(\Re\Psi(\tau-ih)\ge\Psi(T)/2>|h|\).
The original outside radicals have upper bound
\(N^2e^{N|h|}\); they are therefore smaller than the low
complete factors on the entire neighborhood. The full original
outside kernels consequently have the same upper phase.

At fixed positive trace heights, the original double-pole
denominators are bounded after their \(e^{-Nh_i}\) factors
are extracted. At fixed nonzero wire height, the wire
denominator has the bound
\(C e^{-2\pi N(-y)_+}\). On a half-grid side that bound holds
with \(C=1\), even at zero height. All remaining factors and
Jacobians cost only powers of \(N\). The uniform factorial
bound therefore proves (32) for the actual density, through
both parities. Cauchy estimates on slightly enlarged compact
sets retain fixed derivatives in the selected colors. Ordinary
selected-color normals are allowed since \(|\sin t|\ge\sin T>0\)
on the real set, and a smaller fixed positive lower bound holds
on a sufficiently small complex neighborhood. \(\square\)

This estimate covers both reflected factors near the real
contour. A configuration with only one reflected trace factor,
the connectors to the geometric-height contours, and the
projected-kernel terms in a support block are not included.
No nonzero global coefficient follows from (32) alone.

The rational comparisons (28)–(31) are reproduced by
[the pair scalar checker](../experiments/check_real_pair_geometry_and_tail_gap.py).
Its saved record distinguishes these comparisons from the written
height-descent and contour arguments.

## 6. A mixed corner cannot be estimated by lowering both traces

The analogous small-height estimate is false when exactly one
factor is reflected. This is already an obstruction for the original
double-pole density at powers \((3,3)\); it is not a statement about
the signed integral of that density.

At the limiting real corner
\[
             \xi=\frac14,\qquad \tau=\frac\pi2,
             \qquad \rho=0,
 \tag{33}
\]
the first trace is at its factorial wall and the second is regular.
The complete upper exponent is
\[
 \begin{split}
 R_*&=V_{\pi/2}(1/4)+V_0(1/4)+\Psi(\pi/2)+\Psi(0)\\
    &=\frac74M_\infty+\Psi(\pi/2)
      >\frac{5937}{2000}>\frac{29}{10}.
 \end{split}
 \tag{34}
\]
Here \(V_{\pi/2}(1/4)=M_\infty/4\) and
\(V_0(1/4)=M_\infty/2\). The elementary Catalan lower bound
\(G>1-1/9+1/25-1/49\), together with \(\pi<22/7\), gives
\(M_\infty>23/20\). The
[complete-edge gap proof](research_internal_pair_complete_edge_gap.md)
gives \(\Psi(\pi/2)>239/250\). In contrast, the exact enclosure
in the [three-crossing pair certificate](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_three_mixed_packet.md)
gives \(M_{3,3}<13/5\).

**Proposition 5.** There are strictly mixed points with arbitrarily
small positive wire and trace heights at which the original density
has exponential rate greater than \(29/10\), through both parities.
Thus no uniform absolute bound below \(M_{3,3}\) holds on the entire
mixed sector at small heights.

*Proof.* For a sufficiently small fixed \(\epsilon>0\), take
\[
 \begin{gathered}
 x_\epsilon=\frac14-\epsilon+i\epsilon^2,\qquad
 t_\epsilon=\frac\pi2+3\pi\epsilon-i\pi\epsilon^2,\\
 r_\epsilon=\epsilon-3\pi i\epsilon^2.
 \end{gathered}
 \tag{35}
\]
The wall is \(\pi-2\pi\Re x_\epsilon=\pi/2+2\pi\epsilon\).
Consequently \(t_\epsilon\) is strictly reflected and
\(r_\epsilon\) is strictly regular. The sole negative-real-part
factorial argument is
\(1/2-x_\epsilon-t_\epsilon/(2\pi)
=-\epsilon/2-i\epsilon^2/2\).
Its imaginary part is nonzero. In its exact reciprocal reflection,
one cosine exponential therefore dominates the other by a factor
exponential in \(N\). All other factorial arguments stay in regular
strips. Sectorial Stirling and the exact reflection thus give the
actual logarithmic rate \(\mathfrak b\) for both Newton factors,
not merely an upper bound.

The full complete-end kernels have nonzero logarithmic asymptotics
on a fixed complex neighborhood of the pair box, including its
real points \(0\) and \(\pi/2\). This applies at (35) when
\(\epsilon\) is small enough. Since all three heights in (35)
are fixed and positive, the wire and folded trace denominators tend
to one after the original factors \(e^{-Nh_1-Nh_2}\) are extracted.
The sine factors are nonzero, and all remaining normalization
factors have only polynomial size or modulus one. Hence
\[
 \lim_{N\to\infty}\frac1N
     \log|\mathcal I_N(x_\epsilon,t_\epsilon,r_\epsilon)|
       =\mathcal E_{3,3}(x_\epsilon,t_\epsilon,r_\epsilon)
       >\frac{29}{10}
 \tag{36}
\]
for every sufficiently small fixed \(\epsilon\), by continuity
and (34). The same limit holds along either parity. The lower
bound is uniform on a sufficiently small fixed horizontal
neighborhood of this point, so taking the absolute value before
integrating that neighborhood does not remove the obstruction.
\(\square\)

This rules out lowering both trace heights throughout the mixed
sector and then estimating every piece separately. It leaves open
an asymmetric contour that retains the regular trace at its
geometric height, and any exact grouping that preserves cancellation.

## 7. A mixed region that can be kept near the real contour

The obstruction in Section 6 does not occur throughout the shared
index interval. There is a uniform gap when its real coordinate is
at most \(1/8\). One trace angle may then be anywhere in the
retained real interval, provided the other is beyond its factorial
wall. This supplies a larger region on which small contour heights
are permitted; it does not construct the connecting contours.

**Lemma 6.** For \(0<\xi\le1/8\),
\(\pi-2\pi\xi\le|\tau|<\pi\), and \(|\rho|<\pi\),
\[
 V_\tau(\xi)+\Psi(\tau)+V_\rho(\xi)+\Psi(\rho)
       <\frac{5953}{2400}
       =\frac{63}{25}-\frac{19}{480}.
 \tag{37}
\]
The same statement holds with the trace angles exchanged.

*Proof.* Put
\[
 C(\xi)=J(2\xi)-2J(\xi)+\Psi(\pi-2\pi\xi),
 \qquad V_0(\xi)=-2J(1/2-\xi)-2J(\xi).
 \tag{38}
\]
Lemma 3 bounds the reflected factor by \(C(\xi)\).
The monotonicity in (26) bounds the other factor by
\(V_0(\xi)+M_\infty\). The function \(C\) increases on
\((0,1/4]\), as proved there, and
\(V_0'(\xi)=2\log\cot(\pi\xi)>0\) on \((0,1/4)\).
Their sum is therefore at most its value at \(\xi=1/8\).

Here that value can be bounded without numerical optimization.
The sine duplication identity and the Fourier blocks in (27) give
\[
 \begin{gathered}
 J(1/4)=2J(1/8)-2J(3/8),\qquad J(1/4)=-M_\infty/8,\\
 -8J(1/8)=\Psi(\pi/2)+M_\infty/4,\\
 C(1/8)+V_0(1/8)+M_\infty
   =\frac{15}{16}M_\infty+\frac34\Psi(\pi/2)+\Psi(3\pi/4).
 \end{gathered}
 \tag{39}
\]
For the third identity, the absolutely convergent sine series for
\(-2\pi J(1/8)\) has odd-index part
\((\sqrt2/2)\sum_{j\ge0}b_j\) and even-index part \(G/4\).
Equation (27) proves the identity, with all constants fixed.

It remains to bound \(\Psi(3\pi/4)\). On
\([\pi/2,3\pi/4]\),
\[
 \Psi'(t)=-\frac{\operatorname{asinh}\tan(t/2)}\pi,
 \quad \Psi''(t)=-\frac{\sec(t/2)}{2\pi},
 \quad \Psi'''(t)=-\frac{\sec(t/2)\tan(t/2)}{4\pi}
                     \le-\frac{\sqrt2}{4\pi}.
\]
Taylor's formula with integral remainder, starting at \(\pi/2\),
therefore gives
\[
 \begin{split}
 \Psi(3\pi/4)
 &\le\Psi(\pi/2)-\frac{\operatorname{asinh}1}{4}
                  -\frac{\sqrt2\pi}{64}
                  -\frac{\sqrt2\pi^2}{1536}\\
 &<\frac{24}{25}-\frac7{32}
       -\frac{(7/5)(25/8)}{64}
       -\frac{(7/5)(25/8)^2}{1536}
   =\frac{1631821}{2457600}<\frac23.
 \end{split}
 \tag{40}
\]
We used \(\sqrt2>7/5\), \(\pi>25/8\), and
\(\operatorname{asinh}1>7/8\). The last elementary lower bound
follows from \(\sqrt2>140/99\): if \(r=\sqrt2-1>41/99\), then
\[
 \operatorname{asinh}1=\log(1+\sqrt2)
       =2\operatorname{artanh}r
       >2\left(\frac{41}{99}+\frac{(41/99)^3}{3}\right)
       =\frac{2548888}{2910897}>\frac78.
\]
Finally insert (40), \(M_\infty<7/6\), and
\(\Psi(\pi/2)<24/25\) into (39). The resulting upper bound is
\((15/16)(7/6)+(3/4)(24/25)+2/3=5953/2400\).
This proves (37). \(\square\)

Fix \(0<\alpha<1/8\) and \(T<\pi\). Omit empty sections of
the following compact real set:
\[
 \alpha\le\xi\le1/8,\qquad
 \pi-2\pi\xi\le|\tau|\le T,\qquad |\rho|\le T.
 \tag{41}
\]
The second trace may itself be reflected, but need not be.

**Proposition 7.** For each fixed integer pair \(n,p\ge3\),
there is \(\varepsilon>0\) such that the original density (4)
in the [horizontal-contour note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md)
satisfies
\[
 |\mathcal I_N(\xi+iy,\tau-ih_1,\rho-ih_2)|
       \le CN^A\exp\{N(M_{n,p}-19/960)\}
 \tag{42}
\]
on (41), for fixed \(0<h_1,h_2<\varepsilon\) and
\(0<|y|<\varepsilon\). The estimate is uniform when those
nonzero heights range over compact sets. On half-grid wire sides
\(N\xi\in\mathbb Z+1/2\), it holds also for \(y=0\).
It holds with the two traces exchanged, and after any fixed number
of selected ordinary color derivatives.

*Proof.* At zero heights, the real crossing factors have modulus
one, so Lemma 6 bounds the full exponent by
\(63/25-19/480<M_{n,p}-19/480\). The continuous
reciprocal-factorial upper exponent is uniformly continuous on a
compact neighborhood of (41), including its zeros. Choose
\(\varepsilon\) so the change in the full exponent is less than
\(19/960\), with a strict margin on a slightly larger neighborhood.

As in Proposition 4, \(T<\pi\) puts the actual low complete
kernels inside their logarithmic-phase domain for all sufficiently
small heights. Their real phases are at least \(\Psi(T)>0\).
Shrinking \(\varepsilon\) makes the outside radicals, bounded by
\(N^2e^{N|h_i|}\), exponentially smaller than those low kernels.
Thus the full original outside factors have the required upper
phase. The exact trace denominators and wire denominator obey
the bounds used in Proposition 4. In particular a half-grid wire
side has no wire pole even at height zero.

The angle \(\rho=0\) is allowed in (41), so an ordinary normal
in that variable must not be bounded by dividing by \(\sin\rho\).
At the stated positive trace heights,
\(|\sin(\rho-ih_2)|\ge\sinh h_2>0\); the same bound holds for
the other trace. Cauchy estimates on smaller neighborhoods of
these fixed contours therefore retain all specified normals at a
polynomial cost. This proves (42) through both level parities.
\(\square\)

The new estimate covers the left part of the mixed sector. The
interval \(1/8<\xi<1/4\), the connecting contours, and the
projected-kernel terms remain outside its scope. Section 6 explains
why extending the same small-height argument to that whole interval
is impossible. The rational bounds (39)–(42) are included in
the existing pair scalar checker; the contour implication is the
written argument above.

## 8. Retaining the regular trace height removes part of the obstruction

The mixed corner in Section 6 has a strict gap if the regular trace
keeps a sufficiently large positive height. The following criterion
is conditional on that height; it is not a lower bound for every
geometric height in the pair family.

For real \(0<\xi\le1/4\), define
\[
 B_\xi(H)=\Re\{b(\xi,-iH)+\Psi(-iH)\}-H.
\]
All its factorial arguments have positive real part. Direct
differentiation on the original branches gives
\[
 B_\xi'(H)
 =-1+\frac{
       \arctan(\tan(\pi\xi)\tanh(H/2))
                  +\arcsin(\tanh(H/2))}{\pi}
 \le -1+\frac H\pi.
 \tag{43}
\]
Indeed \(\tan(\pi\xi)\le1\) and
\(\arctan(\tanh(H/2))\le H/2\).
Also \(\arcsin(\tanh z)\le z\) for \(z\ge0\), since
its derivative is \(\operatorname{sech}z\le1\).
Thus
\(B_\xi(H)\le V_0(\xi)+M_\infty-H+H^2/(2\pi)\).

**Lemma 8.** Suppose \(0<\xi\le1/4\),
\(\pi-2\pi\xi\le|\tau|<\pi\), and
\(3/5\le H\le107/100\). At wire height zero, reflected
trace height zero, and regular trace \(r=-iH\), the full
upper exponent obeys
\[
 \begin{split}
 \mathcal E_{n,p}(\xi,\tau,-iH)
 &\le \frac74M_\infty+\Psi(\pi/2)-H+\frac{H^2}{2\pi}\\
 &<\frac{1801}{600}-\frac35+\frac{36}{625}
   =\frac{63}{25}-\frac{911}{15000}
   <M_{n,p}-\frac{911}{15000}.
 \end{split}
 \tag{44}
\]
This statement concerns the exponent at the real wire and reflected
trace, not a density evaluated at its finite real poles.

*Proof.* Lemma 3 bounds the reflected factor by
\(M_\infty/4+\Psi(\pi/2)\), while
\(V_0(\xi)\le V_0(1/4)=M_\infty/2\).
Equation (43) supplies the regular factor including its original
\(e^{-NH}\) trace weight. Both crossing Gaussians have modulus one
at these particular arguments. This proves the first line of (44).
Use \(M_\infty<7/6\), \(\Psi(\pi/2)<24/25\), and the
fact that \(-H+H^2/(2\pi)\) decreases on this height interval.
At \(H=3/5\), \(\pi>25/8\) gives
\(H^2/(2\pi)<36/625\). The rational subtraction in (44)
and \(M_{n,p}>63/25\) finish the proof. \(\square\)

**Proposition 9.** Fix integer powers \(n,p\ge3\),
\(0<\alpha<1/4\), and \(T<\pi\). There is
\(\varepsilon>0\) such that the original double-pole density
has a uniform bound on
\[
 \begin{gathered}
 \alpha\le\xi\le1/4,\qquad
       \pi-2\pi\xi\le|\tau|\le T,\qquad
       3/5\le H\le107/100,\\
 x=\xi+iy,\quad t=\tau-ih,\quad r=\rho-iH,
 \qquad 0<|y|<\varepsilon,\quad
       0<h<\varepsilon,\quad |\rho|<\varepsilon:
 \end{gathered}
 \tag{45}
\]
namely
\[
 |\mathcal I_N(x,t,r)|
       \le CN^A\exp\{N(M_{n,p}-911/30000)\}.
 \tag{46}
\]
The constant is uniform when the nonzero small heights range over
compact sets. Half-grid wire sides allow \(y=0\) as well.
The traces may be exchanged, and any fixed selected ordinary-color
normal has the same upper exponent.

*Proof.* Apply uniform continuity of the complete exponent to the
compact set in Lemma 8, losing less than half its strict gap.
This includes the original crossing term \(p\rho H/(2\pi)\);
the allowed \(\varepsilon\) depends on the fixed powers.
The continuous factorial upper bound remains valid through the
reflected wall. For the regular trace, the full complete-kernel
logarithmic theorem applies near the compact segment
\(\{-iH:3/5\le H\le107/100\}\). It includes zero real angle.
For the other trace, \(T<\pi\) and the small reflected height
give the full-kernel normalization exactly as in Proposition 4.
The original trace denominators and wire denominator then give
their stated exponential weights, with polynomial prefactors.
Finally \(|\sin r|\ge\sinh(3/5)\) and the reflected trace
stays a fixed distance from angles \(0,\pi\). Cauchy estimates
on smaller neighborhoods therefore retain the specified normals.
\(\square\)

The certified height \(H_{3,3}=0.959763584\ldots\) lies strictly
inside this interval. Thus this asymmetric choice removes the
specific large corner of Section 6 for that pair. The criterion
does not cover geometric heights below \(3/5\), regular angles
outside the small neighborhood in (45), or any connectors to
these contours. Those require separate coupled estimates.

## 9. A trace height matched to the wire height

There is a useful choice of heights for a whole reflected angular
interval. Keep the upper wire at height \(Y>0\) and put the reflected
trace at height \(h=2\pi Y\). Its reflected factorial argument then
has zero imaginary part. The real upper phase decreases with its
positive angular coordinate, under the geometric height condition
specified below. Thus its maximum is on the factorial wall, rather
than at an unknown interior angle.

For this section write
\[
 E_n(\xi,\tau;Y,h)
 =\mathfrak b(\xi+iY,\tau-ih)+\Re\Psi(\tau-ih)
                         +\frac{n\tau h}{2\pi}-h.
 \tag{47}
\]
The function \(\Psi\) has the original holomorphic continuation in
the strip \(0<\Re t<\pi\). This definition is a phase comparison.
Using it as an upper bound for the full finite kernel additionally
requires its logarithmic normalization or a separate upper bound
on the chosen contour. That requirement is not inferred just from
the continuation of \(\Psi\).

**Lemma 10.** If \(0<h\le3/4\) and \(\pi/2<\tau<\pi\), then
\[
 \begin{split}
 K_h(\tau)
 :={}&\Re\operatorname{asinh}\tan((\tau-ih)/2)\\
 &+\frac14\log
   \frac{\cos^2((\tau-\pi/2)/2)+\sinh^2h}
        {\sin^2((\tau-\pi/2)/2)}
       >\frac12\log34>2\operatorname{asinh}1 .
 \end{split}
 \tag{48}
\]

*Proof.* Put \(u=\tau-\pi/2\), \(v=\tan(u/2)\), so \(0<v<1\).
The logarithmic identity for the inverse hyperbolic sine gives
\[
 \Re\operatorname{asinh}\tan((\tau-ih)/2)
  =\operatorname{artanh}
       \frac{\sin(\tau/2)}{\cosh(h/2)}.
 \tag{49}
\]
For example, use
\(\operatorname{asinh}\tan(t/2)=\log\tan(\pi/4+t/4)\)
on the branch through \(t=0\), then take the squared modulus
of the tangent. Its argument in (49) lies strictly between zero
and one, so no logarithmic branch choice remains in that real
formula.

Use the following rational bounds:
\[
 \begin{array}{c|cc}
 \text{height interval}&\cosh(h/2)<C&\sinh h\ge S\\ \hline
 0<h\le1/2&1033/1000&0\\
 1/2\le h\le3/4&134/125&1/2 .
 \end{array}
 \tag{50}
\]
Both upper bounds follow from
\(\cosh z\le1+z^2/[2(1-z^2/12)]\) at \(z=1/4,3/8\).
For either row define
\[
 A=(1+v)^2,\qquad B=2C^2(1+v^2),\qquad
 D=1+(1+v^2)S^2,\qquad a=\sqrt{A/B}.
\]
Then \(0<a<1\), and (49) bounds (48) from below by
\(\operatorname{artanh}a+\frac14\log(D/v^2)\).
It suffices to prove
\[
                    \frac{1+a}{1-a}>\frac{34v}{\sqrt D}.
 \tag{51}
\]
Indeed (51), after squaring, says that the exponential of four
times that lower bound exceeds \(34^2\).

For \(0<v\le1/8\), one has \(a>13/20\). To check it, use
\((1+v)^2/(1+v^2)\ge1\) and
\(2(134/125)^2(13/20)^2<1\).
Consequently the left side of (51) exceeds \(33/7\), whereas
its right side is at most \(17/4\).

For \(1/8\le v\le1\), consider the explicit degree-eight polynomial
\[
 P_{C,S}(v)=4624v^2D(B+A)^2-(B-A)^2(D+1156v^2)^2 .
 \tag{52}
\]
It is strictly positive on this interval. Here is an exact
certificate with small rational inputs. If
\(P(v)=\sum_{k=0}^8p_kv^k\), its Bernstein coefficients on
\([a_0,b_0]\) are
\[
 \beta_i=\sum_{j=0}^i\frac{\binom ij}{\binom8j}
       (b_0-a_0)^j
       \sum_{k=j}^8p_k\binom kj a_0^{k-j},
                    \qquad 0\le i\le8 .
 \tag{53}
\]
Expanding (52) in (53) gives the following rational lower bounds
for every coefficient in the indicated row:

| \(C\) | \(S\) | Interval | Lower bound for every \(\beta_i\) |
|---|---|---|---|
| \(1033/1000\) | \(0\) | \([1/8,1]\) | \(555\) |
| \(134/125\) | \(1/2\) | \([1/8,9/16]\) | \(747\) |
| \(134/125\) | \(1/2\) | \([9/16,1]\) | \(12130\) |

The Bernstein basis functions are nonnegative and sum to one,
so these exact rational comparisons prove \(P_{C,S}>0\).
The existing scalar checker forms (52) by rational polynomial
multiplication and reproduces all 27 comparisons; it does not
sample the polynomial or approximate its roots.

To see explicitly why this suffices, put \(R=34v/\sqrt D\).
Since \(B>A>0\), (52) implies
\[
 2R(1+a^2)>(1-a^2)(1+R^2),
 \qquad
       a^2(1+R)^2>(R-1)^2 .
\]
Thus \(a>(R-1)/(R+1)\), proving (51). This proves the first
inequality in (48). For the second, note that
\((1+\sqrt2)^4=17+12\sqrt2<34\), since \(\sqrt2<17/12\).
Taking logarithms proves it. \(\square\)

**Proposition 11.** Let \(Y,H_n\) be the original wire and trace
heights of a fixed positive pair \(n,p\ge3\). Suppose
\[
                         h=2\pi Y\le H_n .
 \tag{54}
\]
For \(0<\xi\le1/4\) and \(\pi-2\pi\xi<\tau<\pi\),
\[
 \frac{\partial}{\partial\tau}E_n(\xi,\tau;Y,h)
       <-\frac{\delta_*}{\pi},\qquad
 \delta_*=\frac12\log34-2\operatorname{asinh}1>0.
 \tag{55}
\]
The comparison integrates from the wall
\(\tau=\pi-2\pi\xi\), where the derivative has an integrable
logarithmic singularity.

*Proof.* The [geometric wire-height bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_angular_tail_transport.md#2-a-uniform-bound-on-the-actual-pairs-wire-height)
gives \(0<h<3/4\).
At these matched heights,
\[
 \begin{split}
 \partial_\tau E_n
 &=\frac{nh}{2\pi}-\frac{k_0+k_\xi}{\pi},\\
 k_0&=\Re\operatorname{asinh}\tan((\tau-ih)/2),\\
 k_\xi&=\frac14\log
   \frac{\cos^2(\pi\xi-\tau/2)+\sinh^2h}
        {\cos^2(\pi\xi+\tau/2)} .
 \end{split}
 \tag{56}
\]
This follows by differentiating the real factorial primitive;
on its negative real argument either continuation has the same
real derivative. The denominator vanishes only at the wall.

For fixed \(\tau\), set \(b_0=\pi/2-\tau/2\) and \(a_0=\pi\xi\).
The reflected condition is \(0\le b_0<a_0\le\pi/4\), and the
ratio in (56) becomes
\[
 \frac{\sin^2(a_0+b_0)+\sinh^2h}{\sin^2(a_0-b_0)}.
\]
Its logarithmic derivative in \(a_0\) is at most
\(2\cot(a_0+b_0)-2\cot(a_0-b_0)\le0\).
Consequently \(k_\xi\ge k_{1/4}\), and Lemma 10 gives
\(k_0+k_\xi>\frac12\log34\).

It remains to use the actual periods, rather than a free
height parameter. Write the geometric trace angles as
\(t_n=a_n-iH_n\) and \(t_p\). Their original imaginary period
equation is
\[
 \frac{nH_n}{2}
   =\Re\operatorname{asinh}\tan(t_n/2)
       +\Re\operatorname{asinh}
                    \bigl(\tan(t_n/2)\cos(t_p/2)\bigr)
           <2\operatorname{asinh}1 .
 \tag{57}
\]
The angle bound \(0<a_n<\pi/2\) gives
\(\lvert\tan(t_n/2)\rvert^2
 =(\cosh H_n-\cos a_n)/(\cosh H_n+\cos a_n)<1\);
the positive-pair geometry also gives
\(\lvert\cos(t_p/2)\rvert<1\).
Finally \(\Re\operatorname{asinh}z\le\operatorname{asinh}|z|\):
write \(z=\sinh(u+iv)\) on its specified branch and use
\(|z|^2=\sinh^2u+\sin^2v\ge\sinh^2u\).
These facts prove the strict inequality in (57).
Condition (54), (56), and (57) now prove (55).
Continuity of the real primitive and its logarithmic wall
singularity justify integration from the wall. \(\square\)

This proposition covers the positive reflected angular branch
under (54). It does not impose that height ordering on every
positive pair: some geometric pairs have \(H_n<2\pi Y\).
Section 11 compares the negative reflected branch at these same
heights. Connecting contours and portions where the full kernel
needs a different estimate still require their own bounds.
This supplies a uniform direction of phase decrease,
with a proof using the original periods, on the stated region.

## 10. A connected reflected contour with the full outside kernels

The aligned-height estimate reaches a fixed angular interval while
retaining the entire regular trace interval. The full outside
kernels, rather than only their low Newton parts, are controlled
on the rectangle needed for this construction.

**Lemma 12.** Uniformly on a fixed complex neighborhood of
\[
 \mathcal R_1=\{\tau-ih:|\tau|\le2\pi/3,\quad
                                      0\le h\le3/4\},
 \tag{58}
\]
the original complete-end kernel has a nonzero logarithmic
asymptotic \(K_N(-2\cos t,-2)=\exp\{N\Psi(t)+O(\log N)\}\),
through both parities. Every fixed ordinary selected-color normal
has the corresponding polynomial-times-exponential upper bound.

*Proof.* On this rectangle
\(\Re(-2\cos t)\le\cosh(3/4)<79/61<2\).
The [actual low complete-kernel logarithmic theorem](research_even_complete_low_kernel.md#5-consequence-for-the-geometric-exponential-rate)
therefore applies on a neighborhood of its compact spectral image,
with the [original odd-level normalization](research_last_physical_row_riccati.md#5-the-actual-complete-end-kernel-at-odd-levels) at odd levels.
Moreover \(\Re\sec(t/2)>0\) for \(|\Re t|<\pi\).
Since \(\Psi''(t)=-\sec(t/2)/(2\pi)\), imaginary convexity
and its zero height derivative on the real axis give
\(\Re\Psi(\tau-ih)\ge\Psi(\tau)\ge\Psi(2\pi/3)\).

There is a strict rational lower bound for this last value.
The absolutely convergent sine series gives
\[
 \begin{split}
 \Psi(2\pi/3)
 &=\frac4\pi\sum_{j\ge0}\left\{
 \frac1{2(12j+1)^2}+\frac1{(12j+3)^2}
       +\frac1{2(12j+5)^2}\right.\\
 &\hspace{40mm}\left.
       -\frac1{2(12j+7)^2}-\frac1{(12j+9)^2}
       -\frac1{2(12j+11)^2}\right\}\\
 &>\frac{14513824}{18866925}
   =\frac34+\frac{1454521}{75467700}.
 \end{split}
 \tag{59}
\]
Each block is positive by pairing denominators six apart.
The first block is \(7256912/12006225\); multiply by
\(4/\pi>14/11\) to obtain (59).
Thus \(\Re\Psi(t)-h\) has a fixed positive margin on (58).
The full outside radical has upper bound \(N^2e^{Nh}\), so it
is exponentially smaller than the low kernel, uniformly on a
slightly larger neighborhood. Adding it proves the claimed
nonzero logarithmic asymptotic. The bounds for ordinary normals
follow from holomorphic Cauchy estimates in the spectral variable;
no division by a zero angular sine at \(t=0\) is required.
\(\square\)

Fix a positive integer pair \(n,p\ge3\), with geometric data
\(x_*=\xi_*+iY\), \(t_n=a_n-iH_n\), and
\(t_p=a_p-iH_p\). Suppose
\[
                 L:=2\pi Y\le H_n.
 \tag{60}
\]
The [actual wire-height bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_angular_tail_transport.md#2-a-uniform-bound-on-the-actual-pairs-wire-height)
gives \(0<L<3/4\). Keep the upper wire and the other trace
at \(x=1/4+iY\) and \(r=\rho-iH_p\).

**Proposition 13.** There is \(\delta>0\), depending on the
fixed pair, such that the original full double-pole density is
bounded by \(CN^A e^{N(M_{n,p}-\delta)}\) on both pieces
\[
 \begin{array}{ll}
 \text{wall connector:}&t=\pi/2-is,\quad L\le s\le H_n,\\
 \text{reflected segment:}&t=\tau-iL,\quad
                                    \pi/2\le\tau\le2\pi/3,
 \end{array}
 \qquad -\pi/2\le\rho\le\pi/2.
 \tag{61}
\]
The estimate holds on a fixed tube about their union, through
both parities and with every fixed selected ordinary-color normal.
In particular it covers a fixed neighborhood of \(\xi=1/4\)
and the complete regular-angle intervals
\(|\rho|\le\pi-2\pi\xi\) there.

*Proof.* The closed-wall theorem in the
[right-horizontal bulk note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md#4-the-closed-wall-and-a-fixed-reflected-width)
supplies a strict gap at
\(x=1/4+iY\), \(t=\pi/2-iH_n\), for every displayed
\(\rho\). Proposition 1 lowers the first height from \(H_n\)
to \(L\) without increasing its upper phase. At this closed
wall it follows by continuity from the strict reflected chamber:
take \(\xi\uparrow1/4\), \(\tau\downarrow\pi/2\), with
\(\tau\ge\pi-2\pi\xi\). The original primitive is continuous
at the limiting factorial zero. This proves the same phase gap
along the entire wall connector.

Proposition 11, using (60), then decreases the phase as \(\tau\)
runs from \(\pi/2\) to \(2\pi/3\) at height \(L\).
The regular factor, its crossing, and its trace weight are
unchanged during this step. The same strict gap therefore holds
on the reflected segment, for every regular \(\rho\) in (61).

On the wall connector the first complete kernel is in the proved
[full pair rectangle](research_internal_pair_complete_edge_gap.md#2-a-uniform-gap-on-the-whole-pair-box) \(0\le\Re t\le\pi/2\),
\(0\le-\Im t\le107/100\). On the reflected segment it is
covered by Lemma 12. The other complete kernel stays in the
pair rectangle or its evenness-and-Schwarz reflection. Hence
these are bounds for the full original outside kernels.
The uniform reciprocal-factorial theorem includes the reflected
wall and its zeros. Both trace heights are bounded below by
fixed positive numbers, and the wire height is \(Y>0\), so
their literal denominators have the exponential weights already
included in the phase and bounded remaining factors.

The real upper exponent is continuous on this compact union.
Shrink a fixed tube so that its variation uses less than half
the gap. The same complete-kernel neighborhoods and finite
factorial bounds apply there. Cauchy estimates on smaller tubes
retain selected normals; their angular sines have positive lower
bounds because the trace heights remain positive. This proves
the stated actual-density estimate. \(\square\)

This construction retains the wall connector rather than discarding
it. On sufficiently small fixed shared-index blocks, its angle can
be replaced by the appropriate physical midpoint near \(\pi/2\),
and the other endpoint by a midpoint near \(2\pi/3\). Both
adjustments are \(O(N^{-1})\) and stay in the tube. Thus the
regular contour at height \(H_n\), the displayed connector, and
the reflected segment at height \(L\) form one connected piece
of an original trace contour, with all its first-normal residues
retained. Pointwise trace-contour independence permits this
choice on each fixed shared-index block.

The piece is not a closed trace contour by itself. Its return or
height-change connector at the \(2\pi/3\) end remains in the
exact decomposition and has not been bounded here. Neither the
lower wire nor the cases \(H_n<2\pi Y\) follow from
Proposition 13. The negative reflected segment and its negative
wall connector are supplied at the same heights by Section 11.
Those remaining qualifications
prevent using this connected piece as a global pair estimate.

For a reflected power at least seven, the height ordering (60)
can be removed. The stronger height descent in Proposition 2
permits a smaller endpoint height, chosen for the angular cut.

**Proposition 14.** Fix integers \(n\ge7\), \(p\ge3\), and
\(\pi/2<T<\pi\). There is a fixed
\(0<h\le\min(H_n,1/n)\) such that the full original density
has a strict gap below \(M_{n,p}\) on the connected pieces
\[
 \begin{array}{ll}
 x=1/4+iY,\quad r=\rho-iH_p,&-\pi/2\le\rho\le\pi/2,\\
 t=\pi/2-is,&h\le s\le H_n,\\
 t=\tau-ih,&\pi/2\le\tau\le T.
 \end{array}
 \tag{62}
\]
The conclusion holds on a fixed tube, through both parities,
with fixed selected ordinary-color normals. It requires no
comparison between \(H_n\) and \(2\pi Y\).

*Proof.* Proposition 2 and its continuous closed-wall limit
lower the first trace height from \(H_n\) to any fixed
\(h>0\), without increasing the wall phase. Thus the entire
wall connector in (62) inherits the original right-bulk gap.

Here is the angular comparison at an unequal height. Put
\(L=2\pi Y>0\), \(a=\pi\xi\), and
\(u=\tau/2-(\pi/2-a)\). For
\(0<\xi\le1/4\) and \(\pi-2\pi\xi\le\tau<\pi\),
one has \(0\le u\le a\), and the actual factorial upper
exponent gives
\[
 \begin{split}
 k_\xi&:=\frac14\log
 \frac{\sin^2(2a-u)+\sinh^2((L+h)/2)}
      {\sin^2u+\sinh^2((L-h)/2)}\\
 &\ge\frac14\log\frac{\cosh(L+h)}{\cosh(L-h)}>0,\\
 \partial_\tau\mathcal E
 &=\frac{nh/2-k_0-k_\xi}{\pi},\qquad
 k_0=\Re\operatorname{asinh}\tan((\tau-ih)/2)
       \ge\operatorname{asinh}\sqrt{\operatorname{sech}h}.
 \end{split}
 \tag{63}
\]
To obtain the first inequality, use
\(\sin^2(2a-u)\ge\sin^2a\ge\sin^2u\) and
\(\sin^2a\le1/2\). The ratio
\((q+\sinh^2((L+h)/2))/(q+\sinh^2((L-h)/2))\)
decreases with \(q\), giving (63). This uses the logarithms
of the individual cosine moduli and keeps the original
reflected branch. If its denominator vanishes at the wall,
the inequality is interpreted by its limiting value and then
integrated across the logarithmic singularity.

For \(h\le1/n\le1/7\), one has \(\cosh h<2\) and
\[
 \sinh(3/5)<\frac{30}{47}<\frac7{10}<\frac1{\sqrt2}.
\]
The first bound follows by majorizing the positive sinh series
by \(z/(1-z^2/6)\). Consequently \(k_0>3/5\), whereas
\(nh/2\le1/2\). Equation (63) proves the uniform decrease
\[
                     \partial_\tau\mathcal E
                            <-\frac1{10\pi}.
 \tag{64}
\]
It carries the wall gap along the entire reflected segment in
(62), for every displayed regular angle.

Choose \(h\) smaller, if necessary, so the compact rectangle
\(|\Re t|\le T\), \(0\le-\Im t\le h\) stays in
\(\Re(-2\cos t)<2\), and so \(h<\Psi(T)/2\).
The actual low kernel has its logarithmic normalization there.
Imaginary convexity gives \(\Re\Psi(t)\ge\Psi(T)>2h\),
so its outside radical is exponentially smaller. The full
kernel therefore has the same phase on a neighborhood.
The wall connector and other regular trace remain in their
previous full-kernel rectangles. All literal denominators,
factorial zeros, tubes, and selected normals are handled as in
Proposition 13. This proves the actual-density statement.
\(\square\)

If \(T\) is chosen sufficiently close to \(\pi\), the final
folded endpoint connector can also be handled by the existing
[grouped angular-connector theorem](research_internal_pair_grouped_angular_connectors.md#4-group-with-the-whole-other-trace-before-taking-absolute-values).
First choose its cut and positive endpoint-height allowance;
then decrease \(h\) in Proposition 14 to meet that allowance.
With the exact notation
\(W_{n,N}=H_{n,N}+V_{n,N}+O_{n,N}\) of that theorem,
the endpoint term must be paired with the **whole** other
trace. For \(0<q<1/100\), its established bound is
\[
 |V_{n,N}(x)W_{p,N}(x)|
 \le CN^A e^{N\{3M_\infty/2+2\pi|\Im x|+q\}}
 <CN^A e^{N(M_{n,p}-1/100)}
 \quad (|\Im x|\le Y).
 \tag{65}
\]
This retains the folded endpoint current and the original
physical first normals. It is not a pointwise bound with the
other trace restricted to \(|\rho|\le\pi/2\). In a complete
source decomposition, the exact grouping must therefore be
performed before taking absolute values. The complementary
regular-angle pieces still require their own joint bounds.
Section 12 supplies the corresponding lower-wire connected piece.
Section 11 supplies the negative reflected branch
and wall connector at these same heights. Proposition 14
does not supply a global pair coefficient.

## 11. The negative reflected branch at the same heights

Changing the sign of a reflected trace angle improves the full
upper phase at its original crossing power. This comparison holds
separately on each wire; it does not compare the upper wire with
the lower wire. In particular it preserves a proved gap without
changing either trace height.

For \(\sigma\in\{+1,-1\}\), set
\[
 \begin{split}
 f_{\sigma,\pm}(H)
    &=\mathfrak b(\xi+\sigma iY,\,\pm\tau-iH),\\
 E_{n,\sigma}(\pm\tau,H)
    &=f_{\sigma,\pm}(H)+\Re\Psi(\pm\tau-iH)
                 \pm\frac{n\tau H}{2\pi}-H.
 \end{split}
 \tag{66}
\]
The exponent \(\mathfrak b\) is the original continuous
reciprocal-factorial upper primitive, with its upper and lower
continuations at a negative shifted argument.

**Proposition 15.** If
\[
 0<\xi\le1/4,\qquad Y>0,\qquad
                  \pi-2\pi\xi\le\tau<\pi,
 \tag{67}
\]
then, for every \(H>0\),
\[
 |f_{\sigma,-}(H)-f_{\sigma,+}(H)|<H.
 \tag{68}
\]
Consequently, for every real \(n\ge3\),
\[
 E_{n,\sigma}(-\tau,H)
   <E_{n,\sigma}(\tau,H)
                -\left(\frac{n\tau}{\pi}-1\right)H
   \le E_{n,\sigma}(\tau,H)-\frac H2.
 \tag{69}
\]
The comparison includes the factorial wall by continuity.

*Proof.* First take \(\sigma=+1\). Write
\[
 a=\pi\xi,\quad L=2\pi Y,\quad
 A=a+\tau/2\in[\pi/2,3\pi/4),\quad
 B=a-\tau/2\in(-\pi/2,0].
 \tag{70}
\]
On each continuation the angular derivative is obtained from
the two individual logarithms
\[
 b_t(x,t)=\frac1{2\pi}
       \{\Log\cos(\pi x+t/2)-\Log\cos(\pi x-t/2)\}.
 \tag{71}
\]
Their difference must not be replaced by a principal logarithm
of the quotient. Differentiation in the downward height gives
\(f'_{+,\pm}(H)=\Im b_t(\xi+iY,\pm\tau-iH)\).

Suppose first that \(0<H<L\), and put
\(v_\pm=(L\pm H)/2>0\). The two relevant arguments are
\[
 \begin{split}
 \nu_A(v)&=\arg\cos(A+iv)
       =-\pi+\arctan(q_A\tanh v),\qquad q_A=\tan(\pi-A),\\
 \delta_B(v)&=\arg\cos(B+iv)
       =\arctan(q_B\tanh v),\qquad q_B=\tan(-B).
 \end{split}
 \tag{72}
\]
At \(A=\pi/2\), take \(q_A=+\infty\) and the limiting
argument \(-\pi/2\). Since
\((\pi-A)-(-B)=\pi-\tau>0\), one has \(q_A>q_B\ge0\).
Thus, for every \(v>0\),
\(\pi/2\le\delta_B(v)-\nu_A(v)<\pi\).
For \(g=f_{+,-}-f_{+,+}\), (71) gives exactly
\[
 g'(H)=\frac{
       \delta_B(v_-)-\nu_A(v_-)
        +\delta_B(v_+)-\nu_A(v_+)}{2\pi},
                 \qquad 1/2\le g'(H)<1.
 \tag{73}
\]

For \(H>L\), the positive-angle numerator cosine is in
the upper left quadrant and its denominator is in the upper
right quadrant. Their individual arguments differ by a number
strictly between \(0\) and \(\pi\). For the negative angle,
the numerator is in the lower right quadrant and the denominator
in the lower left quadrant; their argument difference is again
strictly between \(0\) and \(\pi\). Endpoints on an imaginary
or positive real axis give the same strict bounds. Therefore
\[
       0<f'_{+,+}(H)<1/2,\qquad
       0<f'_{+,-}(H)<1/2,\qquad |g'(H)|<1/2.
 \tag{74}
\]

These argument choices are the original factorial continuations.
For the negative trace, the negative shifted argument remains
in the lower half-plane throughout. For the positive trace, it
crosses from the lower to the upper half-plane at \(H=L\).
The real upper primitive is continuous at that crossing.
At the wall its possible \(z\log z\) term is continuous
as well. Equations (73)–(74) give bounded one-sided height
derivatives, so the real primitive is absolutely continuous
across the switch. Finally \(g(0)=0\) by evenness of the
factorial expression in its trace argument. Integrating from
zero, splitting at \(H=L\) when necessary, proves
\(|g(H)|<H\).

Evenness in the trace variable and conjugation of the original
upper/lower primitives give
\[
 \begin{split}
 \mathfrak b(\xi-iY,-\tau-iH)
                  &=\mathfrak b(\xi+iY,\tau-iH),\\
 \mathfrak b(\xi-iY,\tau-iH)
                  &=\mathfrak b(\xi+iY,-\tau-iH).
 \end{split}
 \tag{75}
\]
Hence the difference changes sign on the other wire, proving
(68) for both \(\sigma\). The complete phase satisfies
\(\Re\Psi(-\tau-iH)=\Re\Psi(\tau-iH)\).
The crossing terms in (66) differ by \(-n\tau H/\pi\);
the original unit-charge weight \(-H\) is unchanged.
Since \(n\tau/\pi\ge3/2\), (68) proves (69).
Any lower-wire penalty is independent of this trace sign and
cancels in the comparison. \(\square\)

**Corollary 16.** Every positive-reflected piece in Propositions
13 and 14 has its negative-reflected counterpart at the same
wire and trace heights, with the same exponential gap after
possibly shrinking its fixed tube. This includes the negative
wall-height connectors. The other trace retains its entire
stated regular-angle interval. Both parities and every fixed
selected ordinary-color normal are included.

*Proof.* Apply (69) to the reflected trace, leaving the other
trace and the wire unchanged. On those compact pieces the
reflected height has a fixed positive lower bound, so (69)
supplies a uniform extra phase margin. The full complete-kernel
domains are preserved by evenness and Schwarz reflection:
their original polynomials have real coefficients, and
\(-2\cos(-\tau-iH)=\overline{-2\cos(\tau-iH)}\).
The sine Jacobians and the original trace-denominator moduli
are also unchanged. The same uniform reciprocal-factorial
upper estimates apply on the negative reflected branch with
the continuations used above. Thus the full density has the
claimed gap. Continuity permits fixed tubes, and the same
holomorphic Cauchy estimates retain the normals. \(\square\)

This is an upper-phase comparison, not a ratio estimate for
finite densities: reciprocal factorials may vanish. It uses
the established full-kernel domains of the pieces being
compared, and does not supply a new normalization domain.
In particular (75) is not a comparison of complete densities
between the two wires; their wire penalties and prescribed
source contours remain different. The lower-wire density
bound is established separately in Section 12; the remaining joint
regions and the projected-source currents still require their own
estimates. The folded
endpoint term must retain the whole-other-trace grouping in
(65). No nonzero global pair coefficient follows from this
sign comparison alone.

## 12. A connected lower-wire reflected contour for every positive power

The lower-wire height descent in Proposition 2 works for every
power at least three. At a sufficiently small fixed trace height,
the angular decrease works in this entire power range as well.
The starting gap is the original lower-wire closed-wall bound;
no comparison of the two reflected wire densities is needed.

**Proposition 17.** Fix integers \(n,p\ge3\), the original pair
heights \(Y,H_n,H_p>0\), and \(\pi/2<T<\pi\). Put
\(L=2\pi Y\). There is a fixed height satisfying
\[
 0<h\le\min\left\{H_n,\frac L2,\frac17,
                         \frac1{n+\coth(L/4)}\right\}
 \tag{76}
\]
such that the full original double-pole density has a strict
gap below \(M_{n,p}\) on the connected pieces
\[
 \begin{array}{ll}
 x=1/4-iY,\quad r=\rho-iH_p,
                         &-\pi/2\le\rho\le\pi/2,\\
 t=\pi/2-is,              &h\le s\le H_n,\\
 t=\tau-ih,              &\pi/2\le\tau\le T.
 \end{array}
 \tag{77}
\]
It has the same conclusion on the negative wall and reflected
segment, with \(\pi/2,\tau\) replaced by \(-\pi/2,-\tau\).
All these estimates hold on a fixed tube, through both parities,
and with every fixed selected ordinary-color normal. The other
trace keeps its entire stated regular-angle interval.

*Proof.* The lower-wire part of the
[closed-wall theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md#4-the-closed-wall-and-a-fixed-reflected-width)
gives a strict gap at \(x=1/4-iY\),
\(t=\pi/2-iH_n\), for every displayed \(\rho\). Its
upper exponent already contains the original lower-wire penalty
\(-2\pi Y\). Proposition 2 lowers this trace height from
\(H_n\) to any fixed \(h>0\) without increasing that
exponent. At the closed wall this follows by taking the continuous
limit from \(\xi<1/4\),
\(\tau>\pi-2\pi\xi\), in (20). Thus the entire wall
connector in (77) retains the original strict gap.

For the angular step keep \(x=\xi-iY\),
\(0<\xi\le1/4\), and
\(\pi-2\pi\xi\le\tau<\pi\). Write
\(a=\pi\xi\) and \(u=\tau/2-(\pi/2-a)\), so
\(0\le u<a\le\pi/4\). Differentiating the actual
individual cosine moduli gives
\[
 \begin{split}
 \partial_\tau E_{n,-}
       &=\frac{nh/2-k_0-k_\xi^-}{\pi},\\
 k_0&=\Re\operatorname{asinh}\tan((\tau-ih)/2),\\
 k_\xi^-&=\frac14\log
  \frac{\sin^2(2a-u)+\sinh^2((L-h)/2)}
       {\sin^2u+\sinh^2((L+h)/2)}.
 \end{split}
 \tag{78}
\]
These are derivatives of the original continuous upper primitive.
They do not replace its reflected continuation by a different
logarithmic lift. In the range \(h\le L/2\), both hyperbolic
sines in (78) are strictly positive.

Since \(0\le u\le a\le2a-u\le\pi/2\), the numerator's
sine square is at least the denominator's. Set
\(q=\sin^2u\) and
\(A_\pm=\sinh^2((L\pm h)/2)\). Then
\(0<A_-\le A_+\), and \((q+A_-)/(q+A_+)\) increases
with \(q\). Consequently
\[
 \begin{split}
 k_\xi^-&\ge\frac12\log
                  \frac{\sinh((L-h)/2)}{\sinh((L+h)/2)}\\
 &=-\frac12\int_{(L-h)/2}^{(L+h)/2}\coth v\,dv
       \ge-\frac h2\coth(L/4).
 \end{split}
 \tag{79}
\]
The last inequality uses \((L-h)/2\ge L/4\) and the
decrease of \(\coth v\) for \(v>0\).

For \(\tau\ge\pi/2\) and \(h\le1/7\), the same
explicit bound used in Proposition 14 gives
\(k_0\ge\operatorname{asinh}\sqrt{\operatorname{sech}h}
>3/5\). Equations (76), (78), and (79) therefore imply
\[
 \partial_\tau E_{n,-}
  <\frac{h\{n+\coth(L/4)\}/2-3/5}{\pi}
  \le-\frac1{10\pi}.
 \tag{80}
\]
Integrating from the wall carries its gap along the entire
positive reflected segment in (77). The other trace and the
lower-wire penalty are unchanged.

Decrease \(h\) further, if needed, so that the compact rectangle
\(|\Re t|\le T\), \(0\le-\Im t\le h\) lies in
\(\Re(-2\cos t)<2\), and so that \(h<\Psi(T)/2\).
This is possible because \(T<\pi\) and \(\Psi(T)>0\).
The actual low complete-kernel logarithmic theorem applies there.
Imaginary convexity yields
\(\Re\Psi(t)\ge\Psi(T)>2h\), so the full outside
radical is exponentially smaller. This proves the required
full-kernel normalization on the reflected segment. Along the
wall connector and the other regular trace, use the previously
proved full pair rectangle, together with its evenness and
Schwarz reflection. The trace and wire heights have fixed
positive lower bounds. Their exact denominators therefore have
bounded residual factors after their original exponential weights
are extracted.

The uniform reciprocal-factorial upper estimate retains all
reflection terms and zeros. Continuity of its real exponent
permits a fixed tube about (77), with less than half the strict
gap spent on enlarging the domain. Holomorphic Cauchy estimates
on smaller tubes retain every stated ordinary normal. Finally
Proposition 15 supplies the negative-angle pieces at the same
heights, with an additional phase loss of at least \(h/2\).
This proves the assertion. \(\square\)

As in Proposition 14, fixed physical midpoint adjustments at the
angular ends are \(O(N^{-1})\) and stay in the proved tubes.
If \(T\) is chosen close enough to \(\pi\), decrease \(h\)
also to meet the allowance in the grouped angular-connector
theorem. The final folded endpoint current then obeys (65),
paired with the **whole** other trace before taking absolute
values. That grouping includes its physical first normals.
Proposition 17 controls a connected lower-wire piece for every
positive pair; it does not bound every complementary joint region
or projected-source current, and it does not by itself prove a
nonzero global pair coefficient.

## 13. A coupled angular contour on the right wire interval

The preceding connected pieces can be replaced, on the right
wire interval and for powers at least seven, by one contour
covering all retained trace angles. Its two heights change
together. This avoids introducing independent mixed-height
rectangles, whose corners have not been bounded.

Fix integers \(n,p\ge7\), and write \(H_1=H_n\), \(H_2=H_p\).
The [proved large-power geometry](research_real_pair_geometry_and_tail_gap.md#7-a-global-comparison-for-real-trace-angles)
gives
\[
 H_i<3/10,\qquad L=2\pi Y<2/15,\qquad M_{n,p}>163/50.
 \tag{81}
\]
Use the original density \(\mathcal I_N\) and its complete
upper exponent \(\mathcal E\) from (4) and (20) of the
[right-horizontal bulk note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md).
In particular \(\mathcal E\) includes the lower-wire penalty,
the unit trace charges, and both full complete-end kernels.

**Lemma 18 (simultaneous height convexity).** Put
\(T_\xi=\pi-2\pi\xi\), where \(1/4\le\xi\le2/5\).
For either wire \(x=\xi+\sigma iY\), \(\sigma=\pm1\),
and every \(|\tau|,|\rho|\le T_\xi\), the function
\[
 q(\lambda)=
 \mathcal E\bigl(x,\tau-i\lambda H_1,
                         \rho-i\lambda H_2\bigr)
                  \quad(0\le\lambda\le1)
 \tag{82}
\]
is convex. If at least one of \(|\tau|,|\rho|\) equals
\(T_\xi\), it has a uniform strict gap below \(M_{n,p}\),
over all these parameters.

*Proof.* For one trace write \(t=\tau-ih\) and \(a=\pi\xi\).
Away from a factorial zero, direct differentiation gives
\[
 \frac{\partial^2}{\partial h^2}
 \left\{\mathfrak b(x,t)+\Re\Psi(t)
                       +\frac{n\tau h}{2\pi}-h\right\}
 =\frac{\Re\tan(\pi x+t/2)+\Re\tan(\pi x-t/2)
                         +2\Re\sec(t/2)}{4\pi}.
 \tag{83}
\]
The real parts of the two tangent arguments belong to
\([0,\pi/2]\), because \(|\tau|\le\pi-2a\) and
\(a\ge\pi/4\). The formula
\(\Re\tan(u+iv)=\sin(2u)/(\cos(2u)+\cosh(2v))\)
shows that both terms are nonnegative wherever defined.
Also \(\Re\sec(t/2)>0\) for \(|\tau|\le\pi/2\).
Thus (83) is positive between any singular heights, for
either sign of the wire.

At a wall a shifted factorial can vanish when \(h=L\).
The local term in its real primitive is
\(-\Re(z\Log z)\), up to a continuously differentiable
function, with \(z=\pm i(h-L)/(2\pi)\).
Its contribution is \(|h-L|/4\). The height derivative
therefore has an upward jump of \(1/2\), which preserves
convexity. This is the continuous original upper primitive;
no logarithmic lift is changed at the crossing. Combining
the two one-trace functions proves the convexity of (82).
The wire penalty is independent of \(\lambda\).

At \(\lambda=1\), the closed-wall theorem supplies a
uniform gap \(\delta_{\rm wall}>0\) for both wires and
both trace signs. At \(\lambda=0\), at least one real
angle is reflected, so the
[global real-angle mixed bound](research_real_pair_geometry_and_tail_gap.md#7-a-global-comparison-for-real-trace-angles)
gives \(q(0)<M_{n,p}-1/600\). Convexity implies
\[
 q(\lambda)\le
 (1-\lambda)q(0)+\lambda q(1)
 \le M_{n,p}-\min\{1/600,\delta_{\rm wall}\}.
 \tag{84}
\]
Only the phase is evaluated at zero trace height. No finite
trace-density bound at its real poles is asserted.
\(\square\)

**Theorem 19 (the full right angular surface).** Fix
\(\pi/2<T<\pi\). Let \(T_N=T+O(N^{-1})\) be the original
physical midpoint cut, so \(e^{iNT_N}=-\eta\).
There exist \(\lambda_0>0\), \(\epsilon>0\), and
\(\delta>0\), depending on the fixed pair and the cut, with
the following property. For every
\(x=\xi+\sigma iY\), \(1/4\le\xi\le2/5\), the joint
lower-trace horizontal integral has an exact representation
on the smooth surface
\[
 t=\tau-i\lambda(\tau,\rho)H_1,\qquad
 r=\rho-i\lambda(\tau,\rho)H_2,\qquad
                  -T_N\le\tau,\rho\le T_N,
 \tag{85}
\]
where \(\lambda_0\le\lambda\le1\). The scale equals one
when both \(|\tau|,|\rho|\le T_\xi-\epsilon\), and equals
\(\lambda_0\) whenever one of
\(|\tau|,|\rho|\ge T_\xi+\epsilon\). On this entire
surface the original density, including its pulled-back
two-form Jacobian, is at most
\[
                         C N^A e^{N(M_{n,p}-\delta)}.
 \tag{86}
\]
The integral equals the original product of the two horizontal
integrals at the constant small heights
\(\lambda_0H_1,\lambda_0H_2\). Both parities and all original
physical first normals are retained. Every fixed selected
ordinary-color derivative has the same upper exponent. Here
the differentiated colors are the traced colors \(t,r\);
the two outside colors remain complete.

*Proof.* The compact wall family in Lemma 18 has a strict
phase gap, uniformly in \(\lambda\in[0,1]\). By continuity
of the real factorial upper primitive, including its zeros,
that gap persists on a fixed small angular neighborhood of
the family. Choose \(\epsilon>0\) small enough for this
neighborhood and so that
\(T_\xi+\epsilon<T\) and \(T_\xi+\epsilon<2\pi/3\)
throughout the wire interval.

Independently, the global mixed bound at zero trace height
has gap \(1/600\) on the compact set where at least one
of the two real angles is beyond its wall and both angles
have absolute value at most \(T+o(1)<\pi\).
Uniform continuity, followed by the finite-source conclusion
of that bound, permits a fixed small \(\lambda_0>0\)
at which this whole set has a strict gap. Shrink
\(\lambda_0\) as necessary for the full outside kernels,
as detailed below.

Choose a smooth even cutoff \(\chi_\xi(s)\in[0,1]\) equal
to one for \(|s|\le T_\xi-\epsilon\), and zero for
\(|s|\ge T_\xi+\epsilon\), with uniformly bounded
derivatives on this fixed compact interval of \(\xi\).
Take \(0<\chi_\xi(s)<1\) between those two cut locations.
Set
\[
 \lambda(\tau,\rho)
   =\lambda_0+(1-\lambda_0)\chi_\xi(\tau)\chi_\xi(\rho).
 \tag{87}
\]
If \(\lambda=1\), both angles are in the regular region
at their original geometric heights, and the right-horizontal
bulk theorem gives the gap. If \(\lambda=\lambda_0\),
at least one angle is beyond \(T_\xi+\epsilon\);
the small-height mixed bound applies. If
\(\lambda_0<\lambda<1\), both angles have absolute value
at most \(T_\xi+\epsilon\), and one is within
\(\epsilon\) of its wall. The point lies in the fixed
neighborhood of the wall family controlled by (84).
These three cases give a uniform phase gap on (85).

For clarity, these are bounds on the full finite density.
The central and transition pieces have
\(|\Re t|,|\Re r|<2\pi/3\) and heights at most \(3/10\),
so Lemma 12 supplies the full complete-kernel normalization.
On the outer small-height piece, choose \(\lambda_0\)
so that the entire rectangle of real angles up to \(T+o(1)\)
stays in \(\Re(-2\cos t)<2\) and
\(\Re\Psi(t)>|\Im t|\), and similarly for \(r\).
The actual low complete kernels have their proved phase
there, and the full outside radicals are exponentially
smaller. All selected trace heights are bounded below by
the fixed positive numbers \(\lambda_0H_i\). The original
trace denominators and the wire denominator consequently
have their stated exponential weights with bounded residual
factors. The uniform reciprocal-factorial upper bound keeps
all its reflected terms and zeros. Smaller complex
neighborhoods and Cauchy estimates give the stated normals.

It remains to justify the source equality. Start with the
product horizontal rectangle at the constant heights
\(\lambda_0H_1,\lambda_0H_2\), and use the homotopy
\[
 \lambda_s=\lambda_0+s\{\lambda(\tau,\rho)-\lambda_0\},
                                      \qquad 0\le s\le1.
 \tag{88}
\]
All its trace heights are strictly positive. The exact
two-form \(\mathcal I_N(x,t,r)\,dt\wedge dr\), with \(x\)
fixed, is holomorphic throughout this homotopy. Its physical
trace poles lie on the real angles; the reciprocal-factorial
continuation introduces zeros rather than omitted poles.
Since \(\lambda=\lambda_0\) on the entire outer boundary,
the homotopy fixes that boundary pointwise. Stokes' theorem
therefore gives equality of the two horizontal integrals,
without discarding any wall, side, or first-normal residue.
The pulled-back Jacobian is exactly
\[
 \frac{dt\wedge dr}{d\tau\wedge d\rho}
       =1-i\{H_1\partial_\tau\lambda
                          +H_2\partial_\rho\lambda\},
 \tag{89}
\]
which has a uniform fixed bound. It preserves the phase
estimate, proving (86). Midpoint changes of size \(O(N^{-1})\)
stay in the same compact neighborhoods. \(\square\)

Choose \(T\) sufficiently close to \(\pi\) and decrease
\(\lambda_0\) also to satisfy the allowances of the
[whole-other-trace connector theorem](research_internal_pair_grouped_angular_connectors.md#4-group-with-the-whole-other-trace-before-taking-absolute-values).
The surface (85) is unchanged from the constant-height product
on its outer boundary. Thus the original folded endpoint
currents and omitted physical-angle terms have precisely
their old grouping, including their intersections. Their
established gap, together with (86), controls the original
right-wire horizontal contribution for \(1/4\le\xi\le2/5\).
This conclusion uses the exact paired source, not a
rowwise approximation to a projected normal defect.
It does not estimate the remaining wire interval or the
wire-side currents needed to close a global contour.

## 14. The right vertical wire side

The vertical side at the retained-index cut \(2/5\) admits
the same coupled contour construction. Here the wire height
and the two central trace heights first vary together. A
second common scaling lowers the trace heights near the
angular boundary. Small positive endpoint heights remove
the singular zero-height limit from the actual finite source.

Put \(\beta=2/5\) and \(T_*=\pi/5\). For
\(\sigma=\pm1\), \(0\le\theta\le1\), define the ideal
central family
\[
 x_\theta=\beta+\sigma i\theta Y,\qquad
 t_\theta=\tau-i\theta H_1,\qquad
 r_\theta=\rho-i\theta H_2,\qquad
                   |\tau|,|\rho|\le T_* .
 \tag{90}
\]

**Lemma 20.** The complete upper phase on (90) has a
uniform strict gap below \(M_{n,p}\). The same is true
on its angular boundary when the two trace heights are
multiplied by any common \(\lambda\in[0,1]\), with the
wire kept at \(x_\theta\).

*Proof.* Write \(s_i=1/2-t_i/(2\pi)=b_i+iS_i\), where
\(\beta\le b_i\le1-\beta\). In the strict regular interior,
set
\[
 u_i=\Re\cot\pi(s_i+x),\quad
 v_i=\Re\cot\pi(s_i-x),\quad
 w=\Re\cot\pi x,\quad d_i=\Re\csc\pi s_i .
 \tag{91}
\]
For every choice of the imaginary parts in (90),
\[
                    u_i\le0,\quad v_i\ge0,\quad w,d_i>0 .
 \tag{92}
\]
Indeed the real parts of \(s_i+x\) belong to \([4/5,1]\),
those of \(s_i-x\) to \([0,1/5]\), and those of \(s_i\)
to \([2/5,3/5]\). These sign statements are independent of
the signs or order of the imaginary heights.

The negative real Hessian contributed by
\(b(x,t_i)+\Psi(t_i)\), in the coordinates \((\Re x,b_i)\),
is exactly
\[
 \pi v_i
   \begin{pmatrix}1&-1\\-1&1\end{pmatrix}
 -\pi u_i
   \begin{pmatrix}1&1\\1&1\end{pmatrix}
 +2\pi\operatorname{diag}(w,d_i).
 \tag{93}
\]
It is positive definite by (92). Add the two contributions
on the shared wire coordinate. Holomorphy changes the sign
of this Hessian when all imaginary coordinates vary on a
line, so the real phase in (90) is convex in \(\theta\).
The original crossing terms, unit charges and lower-wire
penalty are affine in \(\theta\), and do not affect this
convexity. For angles on a factorial wall, take the continuous
limit from the strict regular interior. This also covers a
vanishing shifted argument along part of the ideal family.

At \(\theta=1\), the right-horizontal bulk theorem gives
the gap for both wire signs and all displayed trace signs.
At \(\theta=0\), real-angle monotonicity and the
[real right-cut estimate](research_real_pair_geometry_and_tail_gap.md#8-two-useful-endpoint-cuts)
give
\[
 \mathcal E(\beta,\tau,\rho)
 \le 2V_0(2/5)+2M_\infty
       <\frac{97}{30}<M_{n,p}-\frac2{75}.
 \tag{94}
\]
Convexity between these two endpoints proves the first
assertion, uniformly on the compact central family.

On its angular boundary, one trace has real part
\(\pm T_*=\pm(\pi-2\pi\beta)\). At the fixed wire
\(x_\theta\), Lemma 18's one-trace calculation proves
convexity when both trace heights are scaled by
\(\lambda\). It applies to every wire height in
\([-Y,Y]\), including zero, by continuity. The
\(\lambda=1\) endpoint is already bounded by the first
assertion. At \(\lambda=0\), the global mixed real-angle
bound has gap \(1/600\). Their convex interpolation
proves the second assertion. \(\square\)

**Theorem 21 (the original right-side current).** Let
\(\beta_N=\beta+O(N^{-1})\) be a physical half-grid cut,
so \(N\beta_N\in\mathbb Z+1/2\). The original vertical
wire contribution on
\[
                 x=\beta_N+iy,\qquad -Y\le y\le Y,
 \tag{95}
\]
has upper bound \(CN^A e^{N(M_{n,p}-\delta)}\) for some
fixed \(\delta>0\). This includes the full paired trace,
its folded endpoint currents and its omitted physical-angle
terms, with the original first normals at both parities.
The two outside colors are complete.

*Proof.* Choose a fixed \(T<\pi\), sufficiently close to
\(\pi\) for the whole-other-trace connector theorem.
By Lemma 20 and uniform continuity, its central and
angular-boundary gaps persist on fixed neighborhoods.
The global mixed real-angle estimate controls the
complement of the square \(|\tau|,|\rho|\le T_*\)
at sufficiently small positive trace heights.
Choose a smooth even cutoff \(\chi\) equal to one on
\([-T_*+\epsilon,T_*-\epsilon]\), zero outside
\((-T_*-\epsilon,T_*+\epsilon)\), and strictly between
zero and one in the two transition intervals. Put
\(\lambda(\tau,\rho)=\chi(\tau)\chi(\rho)\).

Choose fixed small numbers \(0<\varepsilon_i<H_i\).
For \(y=\sigma\theta Y\), use the actual trace heights
\[
 h_i(\theta,\tau,\rho)
       =\varepsilon_i+
             \lambda(\tau,\rho)\theta(H_i-\varepsilon_i).
 \tag{96}
\]
Their difference from the ideal heights
\(\lambda\theta H_i\) is at most \(\varepsilon_i\).
Thus all sufficiently small fixed choices of
\(\varepsilon_i\) retain the compact phase gaps just
proved. In the central region \(\lambda=1\) use (90);
in the transition use the boundary part of Lemma 20;
where \(\lambda=0\) use the small-height mixed bound.
This covers all retained real trace angles
\(-T_N\le\tau,\rho\le T_N\), with
\(T_N=T+O(N^{-1})\) the original midpoint cut.
The \(O(N^{-1})\) displacement from \(\beta\) to
\(\beta_N\) also lies in these fixed neighborhoods.

The complete kernels on the central and transition
parts lie in the proved full pair rectangle, or a
slightly larger neighborhood from Lemma 12. On the
outer part choose \(\varepsilon_i\) small enough that
their low-kernel normalization dominates the outside
radical, exactly as in Theorem 19. All actual trace
heights are at least the positive \(\varepsilon_i\).
On (95), the literal wire factor has the exact bound
\[
 \left|\frac1{1-e^{2\pi iNx}}\right|
   =\frac1{1+e^{-2\pi Ny}}
   \le e^{-2\pi N(-y)_+}.
 \tag{97}
\]
It therefore has the required upper exponent even at
\(y=0\). The uniform factorial estimates and the full
outside kernels now give the actual density bound on
the whole surface.

For every fixed \(x\), deform the constant product
trace heights \((\varepsilon_1,\varepsilon_2)\) to (96).
The outer angular boundary remains fixed, all heights
stay positive, and the exact holomorphic two-form
has no crossed physical poles. The fixed-boundary
Stokes argument of Theorem 19 gives equality of the
integrals. Its Jacobian has a fixed bound. Dependence
of this contour on the wire position introduces no
additional current: this is a pointwise exact trace
identity before the wire integration; equivalently,
the extra \(dx\) terms disappear in
\(dx\wedge dt\wedge dr\). The resulting central
double-horizontal contribution has the claimed gap.

Finally take the \(\varepsilon_i\) within the allowances
of the grouped angular-connector theorem. On the outer
angular boundary they are constant. The exact grouping
with the whole other trace therefore applies without
change, retaining the endpoint-current intersections
and all omitted physical residues. Its bound (65)
has a strict gap for every \(|y|\le Y\). Adding
these terms and integrating over the fixed length
of (95) proves the assertion. \(\square\)

One may take \(\varepsilon_i=\lambda_0H_i\), using the
same small scale as in Theorem 19. At \(y=\pm Y\),
the vertical-side surface then joins that theorem's
right horizontal surface. This matching is convenient;
the pointwise exact trace identities already justify
either choice. The result closes this right wire side,
without replacing the unresolved central wire integral
by an absolute estimate.

