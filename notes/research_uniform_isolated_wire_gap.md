# One wire interval for all nonexceptional isolated fillings

The strict action gap for an isolated filled vertex can be made
uniform over its integer degree and crossing power. This provides a
single interval of retained wire indices for the contour construction.
It does not estimate its central contour.

Use the notation of
[the action-gap theorem](research_isolated_vertex_action_gap.md):
\[
 M_\infty=\frac{4G}{\pi},\qquad
 \Delta_{d,n}=dM_\infty-M_{d,n},\qquad
 \eta_{d,n}=M_{d,n}-(d-1)M_\infty=M_\infty-\Delta_{d,n}.
\]
Here \(G\) is Catalan's constant, \(d\ge1\) is the integer degree,
and \(n\in\mathbb Z\) is the fixed signed crossing power. Assume
\(d+|n|>2\).

**Proposition.** Except at \((d,n)=(2,1),(2,-1),(3,0)\),
\[
                         \eta_{d,n}>\frac16.
 \tag{1}
\]
At the three excluded pairs, \(\eta_{d,n}=0\). At every other pair,
retaining the common wire interval
\[
                       I=[1/128,63/128]
 \tag{2}
\]
leaves an exponential gap greater than \(1/60\) for the original
contribution with at least one wire index outside \(I\), including
its full Hermite trace and every real remaining boundary angle.
The degree and all powers are fixed before the level tends to infinity.

**Proof of the action bound.** The earlier action-gap theorem gives
conjugation symmetry in \(n\), strict decrease of \(\Delta_{d,n}\)
in positive \(n\), and strict decrease of \(\Delta_{d,0}\) in
\(d\ge3\). We may take \(n\ge0\). The elementary bounds used below
are
\[
                    \frac{112}{99}<M_\infty<\frac76.
 \tag{3}
\]
For the lower bound, use \(G>8/9\) and \(\pi<22/7\).
For the upper bound, the alternating series for \(G\) gives
\[
 G<G_+=\sum_{j=0}^{32}\frac{(-1)^j}{(2j+1)^2}.
\]
Machin's identity and alternating bounds for the arctangent give
\[
 \pi>\pi_-
 =16\left(\frac15-\frac1{3\cdot5^3}
                  +\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)
     -\frac4{239}.
\]
The rational inequality \(4G_+<(7/6)\pi_-\) proves the upper
bound in (3).

For \(d\ge4\), monotonicity gives
\(\Delta_{d,n}\le\Delta_{4,0}\). At zero power the exact cone
formula is
\[
 \Delta_{4,0}=2\int_0^1
       \operatorname{arsinh}\tan(\pi\lambda/4)\,d\lambda.
\]
The derivative of \(\operatorname{arsinh}\tan x\) is \(\sec x\).
Convexity of \(\sec x\) on \([0,\pi/4]\) bounds it above by
the chord between its endpoint values:
\[
 \sec x\le1+\frac{4(\sqrt2-1)}\pi x.
\]
Integrating twice gives
\[
 \Delta_{4,0}\le\frac\pi4+\frac{\pi(\sqrt2-1)}{12}
                  =\frac{\pi(2+\sqrt2)}{12}<\frac{44}{49}.
 \tag{4}
\]
The last inequality uses \(\sqrt2<10/7\) and \(\pi<22/7\).
Consequently
\[
 \eta_{d,n}>\frac{112}{99}-\frac{44}{49}>\frac16
 \qquad(d\ge4).
\]

For \(d=3\) and \(n\ge1\), action monotonicity and the proved
degree-power symmetry give
\[
 M_{3,n}\ge M_{3,1}=3M_{1,3}>\frac52.
\]
Here \(M_{1,3}>5/6\) is the strict certified bound in
[the real-angle proof](research_terminal_real_angle_tail.md),
Section 4. It follows from (3) that
\[
 \eta_{3,n}=M_{3,n}-2M_\infty
                  >\frac52-\frac73=\frac16.
\]

For \(d=2\), \(n\ge2\), the earlier estimate
\(\Delta_{2,2}<\pi/4\), together with monotonicity, yields
\[
 \eta_{2,n}>\frac{112}{99}-\frac{11}{14}>\frac16.
\]
For \(d=1\), \(n\ge2\), the terminal value and monotonicity give
\(\eta_{1,n}=M_{1,n}\ge M_{1,2}=M_\infty/2>1/6\).
The three excluded pairs have \(\Delta=M_\infty\), as proved
in the action-gap theorem. This proves (1) for all integer pairs
in the stated range.

**Proof of the uniform interval.** For a low original index put
\[
 J(x)=\int_0^x\log(2\sin\pi v)\,dv,\qquad
 g(x)=J(2x)-4J(x).
\]
The exact derivative is \(g'(x)=2\log\cot(\pi x)\). Since
\(\tan y>y\) for \(0<y<\pi/2\),
\[
 2g(1/128)
 <\frac1{32}\left(1+\log\frac{128}\pi\right)
 <\frac3{20}.
 \tag{5}
\]
For the final inequality, \(\pi>3\), and the finite rational sum
\[
             \sum_{j=0}^{9}\frac{(19/5)^j}{j!}>\frac{128}{3}
\]
implies \(e^{19/5}>128/\pi\). Thus the logarithm in (5) is
less than \(19/5\).

The original Hermite norm bounds give rate at most \(M_\infty\)
for each unrestricted wire and at most \(2g(1/128)\) for a wire
outside (2). The symmetric endpoint is \(1/2-1/128\); the
high-index bound is included. There are only polynomially many
wire assignments at a fixed degree, and the fixed crossing power
and original trace have polynomial norm. Therefore the entire
omitted contribution has rate at most
\[
               (d-1)M_\infty+2g(1/128).
\]
By (1) and (5), its gap below \(M_{d,n}\) exceeds
\(1/6-3/20=1/60\). First normals and all real free boundary
angles are covered by those same original norm estimates.
\(\square\)

The two exceptional degree-two powers have a separate exact
reduction in
[the all-power degree-two theorem](research_all_nonzero_degree_two_fillings.md).
The degree-three zero-power case is treated by the zero-subtree
theory. They need not be forced into an absolute wire-tail estimate
whose limiting gap is exactly zero.

The rational comparisons in this proof can be replayed with
[check_uniform_isolated_wire_gap.py](../experiments/check_uniform_isolated_wire_gap.py).
That script checks finite rational inequalities only. The action
monotonicity, cone formula, and finite-source interpretation are
the written arguments above and in the cited research proofs.
