# The complete endpoint coefficient at the later incoming point

Research deduction, 7 November 2026. The complete endpoint
coefficient has its original nonzero holomorphic asymptotic on a
fixed neighborhood of
\[
                 e_0=\frac14-\frac{i\log2}{4\pi}.
\]
This point lies outside the previously proved endpoint rectangle.
Its auxiliary critical point is real. The proof retains every
revived off-grid row and both finite contour aliases, and does
not require a positive auxiliary critical height.

This supplies an actual endpoint source near the explicit later
point of the continued cap branch. It does not yet estimate the
whole outer cap or the intervening private contour. No numerical
evaluation is used.

## 1. Exact source and the original critical point

Keep the specified finite continuation
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^{l}2\sin(\pi j/N).                              \tag{1}
\]
The Newton polynomials, canonical sine factorial and all
reciprocal zeros are exactly those of
[the complex-index endpoint theorem](research_complete_boundary_complex_index.md).
No row cutoff defines the function in (1). At physical
\(e=j/N\), the rows \(l>j\) vanish; they remain in (1)
at complex \(e\), along both level parities.

At ordinary color \(-2\), use the original phase and critical
action
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad
                    J'(z)=\Log(2\sin\pi z).
 \end{split}                                                     \tag{2}
\]
The branches and the additive constant are unchanged.

Put
\[
 \eta_0=\frac{\log2}{4\pi},\qquad e_0=\frac14-i\eta_0,\qquad
 u_0=\frac1\pi\arctan\frac1{\sqrt2}.                            \tag{3}
\]
The exact later-point calculation in
[the incoming transport theorem, Section 4](research_mixed_half_face_general_incoming_transport.md)
gives
\[
 e^{2\pi ie_0}=i\sqrt2,\qquad
 e^{2\pi iu_0}=\frac{1+2\sqrt2\,i}{3},\qquad
                         F_u(e_0,u_0)=0.                       \tag{4}
\]
In particular (4) has the original zero logarithmic lift.
The endpoint branch is simple, and
\[
                         \frac16<u_0<\frac15.                  \tag{5}
\]
The first inequality follows from
\(\tan(\pi/6)=1/\sqrt3<1/\sqrt2\); the second follows from
\(\tan^2(\pi/5)=5-2\sqrt5>1/2\), using \(\sqrt5<9/4\).

Retain auxiliary real cuts
\[
                           a=\frac1{20},\qquad b=\frac6{25}.    \tag{6}
\]
These are proof cuts only. They will be displaced by
\(O(N^{-1})\) to half-grid cuts in the exact finite residue
identity.

## 2. The regular real segment and its critical action

For \(a\le u\le b\), all three real parts
\(u,1/2-u,\Re(e_0-u)\) lie in \((0,1/2)\). Thus
\[
 -\Re F_{uu}(e_0,u)
 =\pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(e_0-u)\}>0.              \tag{7}
\]
The real path contains the critical point (4). Consequently
its unique nondegenerate real maximum is \(u_0\), and both
real cut values satisfy
\[
 \Re F(e_0,a)<\Re S(e_0),\qquad
                         \Re F(e_0,b)<\Re S(e_0).               \tag{8}
\]
All these gaps are strict fixed numbers; no evaluated minimum
is needed.

We will also use an explicit critical-action floor. For
\(0<d<1/2\), the original sine argument gives
\(\Re J(d-i\eta)\le J(d)\) when \(\eta\ge0\).
By (5), \(1/4-u_0\in(1/20,1/12)\) and
\(1/2-u_0\in(3/10,1/3)\). The analytic inequalities
\[
 -J(1/4)>\frac{14}{99},\qquad
 -J(1/3)>\frac1{12},\qquad
                         -J(1/20)>\frac1{10}                   \tag{9}
\]
therefore yield
\[
 \Re S(e_0)>
       3\frac{14}{99}+\frac16+\frac1{10}
                         =\frac{38}{55}.                       \tag{10}
\]
The first bound in (9) is proved from the alternating Catalan
series in
[the fixed-cut calculation, equations (11)--(12)](research_mixed_next_half_face_fixed_cut_obstruction.md).
For the second,
\[
 -J(1/3)=\int_{1/3}^{1/2}\log(2\sin\pi s)\,ds
                 >\frac1{12}\log3>\frac1{12}.
\]
For the third, \(2\sin\pi s\le2\pi s\) gives
\[
 -J(1/20)\ge\frac1{20}(1-\log(\pi/10))>\frac1{10},
\]
using \(\pi/10<1/3\) and \(\log3>1\).
In (10), the carrier \(+\pi\eta_0u_0\) is positive and has
only been dropped from a lower bound.

## 3. All physical and revived real rows outside the cuts

The original zero-safe row exponent for (1) at complete
color is
\[
 R(e,x)=\mathcal V(x)-J(x)-\Re J_{\rm side}(e-x)
                                      -\pi x\Im e,\qquad
 \mathcal V(x)=2\int_0^x\log(2|\cos\pi s|)\,ds-2J(x).
                                                                    \tag{11}
\]
It bounds every literal row with a polynomial prefactor,
including \(x=0,1\), the odd-level Newton zero, and the
reflected reciprocal zeros. Its source proof and uniform
continuity are in Sections 3--4 of the complex-index theorem.

For \(0<x<1/2\), its derivative is
\[
 \partial_xR(e,x)
  =\log\frac{|\sin\pi(e-x)|\cos^2\pi x}{\sin^3\pi x}
                                      -\pi\Im e.                \tag{12}
\]
This formula uses the appropriate reflected primitive on either
side of \(\Re(e-x)=0\). At \(e=e_0\) the height is nonzero.

For \(0<x\le a\), the real part of \(e_0-x\) is between
\(1/5\) and \(1/4\). Thus its sine modulus exceeds \(1/2\),
\(\cos^2\pi x>1/4\), \(\sin\pi x<1/6\), and
\(e^{\pi\eta_0}>1\). The exponential of (12) exceeds \(27\).
The lower rows are therefore bounded by \(\Re F(e_0,a)\).

For \(b\le x<1/2\), put \(z=\cot\pi x\). One has
\[
                          0\le z<\frac54.                      \tag{13}
\]
Indeed \(\pi x\ge6\pi/25>3/4\), and
\(\tan(3/4)\ge3/4+(3/4)^3/3=57/64>4/5\).
Set \(H=\sinh(\pi\eta_0)\). Exact half-angle algebra gives
\[
 H^2=\frac{3\sqrt2-4}{8}<\frac1{32},\qquad
                         e^{\pi\eta_0}=2^{1/4}<\frac65.         \tag{14}
\]
The first inequality follows from \(\sqrt2<17/12\);
the second from \((6/5)^4>2\).

At this specific real part \(\Re e_0=1/4\), the ratio in
(12), before the carrier \(e^{\pi\eta_0}\), is
\[
 z^2\sqrt{\frac{(1-z)^2}{2}+H^2(1+z^2)}
 \le \frac{z^2|1-z|}{\sqrt2}
                         +z^2H\sqrt{1+z^2}.                    \tag{15}
\]
Both summands have elementary uniform bounds:
\[
 \frac{z^2|1-z|}{\sqrt2}<\frac27,\qquad
                         z^2H\sqrt{1+z^2}<\frac12.              \tag{16}
\]
For \(0\le z\le1\), the first maximum is
\(4/(27\sqrt2)<2/7\). For \(1\le z\le5/4\), it is at most
\(25/(64\sqrt2)<2/7\); the latter squared comparison is
\(30625<32768\). For the second summand, (13)--(14) bound
its square by
\[
                   \frac{25^2\cdot41}{16^2\cdot32\cdot16}
                   =\frac{25625}{131072}<\frac14.
\]
Consequently
\[
                \exp\{\partial_xR(e_0,x)\}
                  <\frac65\left(\frac27+\frac12\right)
                  =\frac{33}{35}<1.                            \tag{17}
\]
Every upper row below the half index, including every
revived row \(x>1/4\), is bounded by \(\Re F(e_0,b)\).

For \(1/2\le x\le1\), the original reflection proof gives
\[
                    R(e_0,x)\le-\Re J(e_0)+2\pi\eta_0.          \tag{18}
\]
For clarity, that proof only requires
\(1/6<\Re e_0<1/2\): after setting \(v=1-x\), its
nonpositive real entropy terms may be dropped, while
\(\Re J(e_0+v)\ge\Re J(e_0)\). The latter follows from
the positive horizontal derivative up to real part \(1/2\)
and the opposite signs of \(\Re J\) in the two half-strips.
Thus the reflection argument of
[the endpoint extension criterion, Lemma 1](research_mixed_endpoint_packet_extension_criterion.md)
applies with the same original forcing and carrier.

The sine-argument bound also gives
\[
 -\Re J(e_0)\le-J(1/4)+\frac{\pi\eta_0}{2}
                      <\frac16+\frac{\pi\eta_0}{2}.
\]
Using \(\log2<7/10\), (18) is therefore strictly less than
\[
                    \frac16+\frac58\log2<\frac{29}{48}.
                                                                    \tag{19}
\]
The floor (10) leaves the explicit positive reserve
\[
                         \frac{38}{55}-\frac{29}{48}
                                      =\frac{229}{2640}.        \tag{20}
\]
No upper row has been deleted by its physical-grid zero or
estimated by an unavailable off-grid endpoint asymptotic.

## 4. The complete finite contour, both aliases and the packet

**Theorem.** There is a fixed complex neighborhood of
\((e_0,-2)\) on which the whole function (1) satisfies
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                    (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
                                                                    \tag{21}
\]
Its phase, coefficient and square-root branch are the original
endpoint ones. Both integer level parities and all fixed joint
ordinary-color and complex-index derivatives are included on
smaller neighborhoods.

*Proof.* Equations (8), (17), and (20) pay all real rows
outside the fixed cuts (6), with a fixed positive gap.
Their zero-safe row exponents are uniformly continuous,
including the reflected cut. The same gaps thus persist
on a sufficiently small fixed complex \(e\)-neighborhood.
The original Newton color bound preserves them after a
further fixed shrink in the ordinary color. At most \(N\)
rows are summed, which costs only a polynomial.

On the retained real segment at \(e=e_0\), the imaginary
part of the original derivative is particularly simple:
\[
 \Im F_u(e_0,x)
      =\Arg\sin\pi(e_0-x)+\frac{\pi}{4}
                    \in(-\pi/4,\pi/4)
                          \qquad(a\le x\le b).                 \tag{22}
\]
The other sine logarithms are real there. All arguments stay
away from their divisors on this compact segment. Choose a
fixed \(h_1>0\), small enough that on the rectangle
\([a,b]+i[-h_1,h_1]\) one still has
\[
                         |\Im F_u|<\frac{\pi}{2},               \tag{23}
\]
and both cut sides have their strict gap from (8).
The latter follows by continuity, reducing \(h_1\) if needed.

Use the original exact finite residue rectangle with its
half-grid cuts and both horizontal heights \(\pm h_1\).
After splitting the cotangent kernel into its constant
part and its two aliases, each horizontal alias has its
exact penalty \(2\pi h_1\). Equations (7) and (23) give
\[
 \Re F(e_0,x\pm ih_1)-2\pi h_1
   \le\Re F(e_0,x)-\frac{3\pi h_1}{2}
   \le\Re S(e_0)-\frac{3\pi h_1}{2}.                            \tag{24}
\]
The entire vertical currents stay on the two paid cut
sides. On half-grid cuts their kernels are bounded, and
splitting off the constant modes retains both original
alias orientations. The unweighted constant-mode path
can be brought to the real segment; its two joining
segments also lie on those paid cut sides.

The real path now passes through the original saddle \(u_0\).
Equation (7) supplies its unique nondegenerate maximum,
and the exact regular row symbol has the original
\(N^{-2}\) power and nonzero amplitude. Its Gaussian
integral therefore has power
\(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\), with the original
branch of \(\sqrt{-F_{uu}}\). The first odd Gaussian
correction integrates to zero. This proves (21) at
\((e_0,-2)\).

All omitted-row gaps, finite horizontal aliases, cut sides
and unweighted joins are strict on fixed compact sets.
They persist on a fixed complex parameter neighborhood.
The implicit critical point moves there inside the same
regular rectangle, and its short path deformation preserves
the cut gaps. The original joint holomorphic factorial
symbol and Gaussian proof give (21) uniformly on that
neighborhood. Since its normalized denominator is nonzero,
Cauchy's estimate supplies every fixed mixed derivative.
No source row or ordinary normal has changed. \(\square\)

The incoming transport theorem identifies \(e_0\) with the
cap critical point at
\[
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\qquad
 a_0=1-\frac{\arg X_0}{2\pi}\in(1/2,7/10).
\]
Thus (21) supplies the actual complete endpoint factor near
this later cap saddle, including its neighborhood where
the auxiliary saddle has either sign of height.
It supplies neither a packet on the whole intervening
private strip nor a bound for the complete outer cap
integral. Those source and contour obligations remain.

