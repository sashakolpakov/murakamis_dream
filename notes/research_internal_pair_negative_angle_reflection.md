# Reflecting negative trace angles in the central wire chamber

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

In the central regular chamber, the original density at a negative
real trace angle is exponentially smaller than the density at its
positive reflection. This comparison keeps the full outside kernel
and the exact double-pole trace factor. It therefore controls a
whole part of the original contour without an asymptotic formula
for a separately contracted vertex.

The comparison is strict away from angle zero. To turn it into a
uniform gap for the entire negative-angle region, one also needs
the positive principal density to have its strict maximum away
from zero. The existing mixed concavity supplies that fact on its
stated domain; it has not been extended here to a reflected
factorial chamber.

## 1. The reflection excess has a finite limit

Use the canonical primitive and wire phase
\[
 J'(z)=\Log(2\sin\pi z),\quad J(0)=0,\qquad
 b(x,t)=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x).
 \tag{1}
\]
The branch of \(J\) is holomorphic on \(0<\Re z<1\).
Fix
\[
 0<\xi<1/4,\qquad 0<\tau<\pi-2\pi\xi,\qquad H>0,
 \quad t=\tau-iH,
 \quad D(y)=\Re b(\xi-iy,t)-\Re b(\xi+iy,t).
 \tag{2}
\]
Every argument in (1) has real part strictly between zero and
one, for all real \(y\). Thus all continuations in this section
remain in the original factorial strips.

**Lemma 1.** For every \(y>0\),
\[
                        0<D(y)<\frac{\tau H}{\pi}.
 \tag{3}
\]

*Proof.* Write \(\cos t=c+id\), where
\(c=\cos\tau\cosh H\), \(d=\sin\tau\sinh H>0\).
The exact reflection derivative from the
[joint alias calculation](research_internal_pair_wire_alias_reflection.md)
is
\[
 D'(y)=\arg\{R_y+i(d+B_y)\}+\arg\{R_y+i(d-B_y)\},
 \quad
 R_y=\cos(2\pi\xi)\cosh(2\pi y)+c,
 \quad B_y=\sin(2\pi\xi)\sinh(2\pi y).
 \tag{4}
\]
When \(R_y>0\), both arguments are in
\((-\pi/2,\pi/2)\). Their sum is positive because the
arctangent is odd and strictly increasing and \(d>0\).
For \(\tau\le\pi/2\), this applies for all \(y\).

If \(\tau>\pi/2\), put \(C=\cos(2\pi\xi)>0\).
The regular-chamber hypothesis gives \(|\cos\tau|<C\).
The function \(R_y\) increases strictly. If it starts
negative, let \(y_0\) be its unique zero. Direct substitution
at that zero gives
\[
 B_{y_0}^2-d^2
   =(\cos^2\tau-C^2)\left(\frac{\cosh^2H}{C^2}-1\right)<0.
\]
Thus both numerator imaginary parts stay positive for
\(0\le y\le y_0\). Their arguments stay in the upper half-plane
and have a positive sum. After \(R_y\) becomes positive the
preceding arctangent argument applies. There is no winding
across the negative real axis. In every case \(D\) is strictly
increasing from \(D(0)=0\).

To compute its limit, the elementary upper and lower half-plane
expansions of the primitive are
\[
 J(z)=
 \begin{cases}
 -\dfrac{i\pi}{2}(z^2-z+1/6)
      +\dfrac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz}),
                                      &\Im z>0,\\[2mm]
 \phantom{-}\dfrac{i\pi}{2}(z^2-z+1/6)
      -\dfrac{i}{2\pi}\operatorname{Li}_2(e^{-2\pi iz}),
                                      &\Im z<0.
 \end{cases}
 \tag{5}
\]
They follow by differentiating, then fixing the constant at zero;
the two formulas have the same boundary values on the real strip.
The dilogarithm terms tend to zero exponentially at large height.
Substituting (5) into (1), with \(x_\pm=\xi\pm iy\), gives
\[
 \begin{split}
 b(x_+,t)&=-i\pi x_+-\frac{it^2}{4\pi}
                         +\frac{i\pi}{4}+o(1),\\
 b(x_-,t)&=\phantom{-}i\pi x_-+\frac{it^2}{4\pi}
                         -\frac{i\pi}{4}+o(1).
 \end{split}
 \tag{6}
\]
In real parts these are \(\pi y-\tau H/(2\pi)+o(1)\)
and \(\pi y+\tau H/(2\pi)+o(1)\). Hence
\(D(y)\to\tau H/\pi\). Strict monotonicity proves (3).
\(\square\)

## 2. Comparison of the exact finite densities

Let \(B_N(x,t)\) be the canonical factorial representative and
\(K_N(t,u)\) the full original outside kernel. For a real outside
angle \(u\), define the trace density, without its constant
scalar, by
\[
 \mathcal D_{n,N}(x,t;u)=
 B_N(x,t)K_N(t,u)\sin t\,
 e^{inNt^2/(4\pi)}
 \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},
 \qquad \eta=(-1)^{N-1}.
 \tag{7}
\]
The full double pole is retained. The density represents the
original first-normal trace; no normal term has been omitted.

**Theorem 2.** On every compact subset of the domain (2), with
\(y>0\), for every fixed real \(n>1\),
\[
 |\mathcal D_{n,N}(\xi+iy,-\tau-iH;u)|
 \le C\exp\left\{-\frac{(n-1)N\tau H}{\pi}\right\}
        |\mathcal D_{n,N}(\xi+iy,\tau-iH;u)| .
 \tag{8}
\]
The bound holds through both level parities, uniformly for all
real outside angles. It also holds when the outside kernel is
replaced by any one of its fixed ordinary outside-color
derivatives.

*Proof.* Evenness and Schwarz reflection give the exact identity
\[
 B_N(\xi+iy,-\tau-iH)
             =\overline{B_N(\xi-iy,\tau-iH)}.
 \tag{9}
\]
The ordinary factorial expansion on the regular strips gives
\[
 B_N(x,t)=\frac{e^{Nb(x,t)}}{2N\sin(\pi x)}(1+O(N^{-1})).
 \tag{10}
\]
Its relative error is uniform on the stated compact sets and
the leading factor is nonzero. Since
\(|\sin\pi(\xi+iy)|=|\sin\pi(\xi-iy)|\), (9)--(10) bound
the ratio of the two wire-factor moduli by \(C e^{ND(y)}\).

The outside kernel has real polynomial coefficients in its
ordinary colors. For real \(u\), its moduli at the two angles
in (8) are exactly equal. The sine factors also have equal
moduli. The two numerators in the trace weight have modulus
\(e^{-NH}\); its denominators are complex conjugates and
therefore have equal moduli. Finally the ratio of the crossing
Gaussian moduli is exactly
\[
 \frac{|e^{inN(-\tau-iH)^2/(4\pi)}|}
      {|e^{inN(\tau-iH)^2/(4\pi)}|}
                         =e^{-nN\tau H/\pi}.
 \tag{11}
\]
Combining this with (3) proves (8). No division by the outside
kernel is necessary, so its possible zeros cause no exception.
Its ordinary derivatives still have real coefficients and the
same reflection property. This proves the final assertion.
\(\square\)

For a joint pair density the shared Cauchy factor is independent
of the trace angles. Applying (8) to either or both factors
therefore reflects the negative real angles independently.
The resulting losses add in the exponent. The other crossing,
outside factor, and exact trace denominator remain unchanged.
If a lower trace graph has an even height function \(H(\tau)\),
the moduli of its reflected parametrization derivatives are
equal as well.

## 3. The remaining qualification at angle zero

On a compact region with \(\tau\ge\tau_0>0\) and
\(H\ge H_0>0\), (8) gives a uniform loss of at least
\((n-1)\tau_0H_0/\pi\). At \(\tau=0\) the reflection is
the same point, so no such loss is possible.

Suppose the positive principal phase on a specified compact
contour has its unique maximum at the actual geometric point,
whose two real trace angles are positive. Its neighborhood of
either zero-angle face then has a strict gap by compactness.
Combine that gap with (8) away from the faces. Every reflected
negative-angle portion is then strictly below the same geometric
rate. The
[mixed concavity theorem](research_mixed_phase_height_extension_and_wire_order.md)
supplies this principal maximum on its stated convex domain.
This argument does not extend its domain or estimate a current
where a factorial leaves its regular strip.

The comparison thus removes negative angles from the central
regular part of the middle-band problem. The remaining task is
a global bound for the positive principal contour and its
transitions through the other middle regions.

## 4. Reproduction

Run `python3 experiments/check_internal_pair_negative_angle_reflection.py`.
The checker compares the primitive reflection with its derivative
formula, verifies the exact elementary factors in (8), and tests
the finite factorial comparison at both parities. The proof of
the uniform bound is (3)--(11), rather than a numerical positivity
test. Its record is
[research-internal-pair-negative-angle-reflection.json](../repro/results/research-internal-pair-negative-angle-reflection.json).
