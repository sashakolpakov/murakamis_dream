# The finite Fourier band of the continued Newton basis

Research theorem, 2 November 2026.

The factorial continuation of a Newton basis element is not periodic
at an arbitrary spectral parameter. At the original spectral values
and their first derivatives, it has a much stronger property: it is
an entire trigonometric polynomial in the continued index. This gives
an exact circle integral for every index occurring in two such
factors. It includes the normal derivatives at repeated roots.

The result provides an exact representation. It does not establish
the dominant geometric cycle of its subsequent angle integrals.

## 1. The algebra and its continued basis

Fix \(N\ge2\), and write \(D=N-1\), \(\eta=(-1)^D\).
The original pair algebra is
\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial specified by
\(T_N(\cos t)=\cos Nt\). Put
\[
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 S_i=\prod_{k=1}^i2\sin\frac{\pi k}{N},\qquad
 e_i(z)=S_i^{-2}\prod_{k=0}^{i-1}(c_k-z),
 \quad 0\le i<N.
 \tag{2}
\]
The distinct roots of (1) have multiplicity two, except for the
simple root \(-2\) when \(N\) is odd. Thus a class in
\(\mathcal A_N\) is specified by its value and first derivative
at each double root, and its value at the possible simple root.

Let \(G_N\) be the canonical sine factorial, with
\[
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),\qquad
 G_N(z)G_N(D-z)=N.
 \tag{3}
\]
Its definition and these identities are proved in the
[factorial note](research_exact_cyclotomic_factorial.md) and
[the boundary-order calculation](research_balanced_factorial_boundary_order.md).
For a complex normalized index \(x\) and an angle \(t\), define
\[
 B_N(x,t)=
 \frac{N}
 {G_N(D/2-Nx+Nt/(2\pi))
  G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{4}
\]
At \(x=i/N\), (3) gives the entire polynomial identity
\[
 B_N(i/N,t)=e_i(-2\cos t).
 \tag{5}
\]
When taking a class of (4) in \(\mathcal A_N\), its values
and derivatives are taken at the original spectral angles
\[
 \tau_j=\pi-\frac{(2j+1)\pi}{N},\qquad
 -2\cos\tau_j=c_j,
 \quad 0\le j\le\lfloor D/2\rfloor.
 \tag{6}
\]
At a double root, \(\sin\tau_j\ne0\), and the derivative
in \(z\) is \((2\sin\tau_j)^{-1}\partial_t\).
At the odd simple root \(\tau_j=0\), only the value is used.

## 2. Explicit spectral values and first derivatives

**Lemma 1.** The value of (4) at (6) is the trigonometric
polynomial
\[
 V_j(x)=\frac{(-1)^{D+j}}N
   \prod_{k=1}^j2\sin\pi(x+k/N)
   \prod_{k=j+1}^D2\sin\pi(x-k/N).
 \tag{7}
\]
At each double root its angular derivative is
\[
 H_j(x)=-\frac12 V_j(x)
                \sum_{k=j+1}^{D-j}\cot\pi(k/N-x).
 \tag{8}
\]
Every apparent pole in (8) is removable. Both (7) and (8)
have frequencies in
\[
 \{-D/2,-D/2+1,\ldots,D/2\}
 \tag{9}
\]
with the convention that a frequency \(a\) means \(e^{2\pi iax}\).

**Proof.** At \(t=\tau_j\), the two shifted arguments in
(4) are \(D-j-Nx\) and \(j-Nx\). Reflection and recurrence
give
\[
 B_N(x,\tau_j)
  =\frac{G_N(j+Nx)}{G_N(j-Nx)G_N(Nx)^2}
  =\frac{\sin\pi Nx}{N\sin\pi x}
     \prod_{k=1}^j
       \frac{\sin\pi(x+k/N)}{\sin\pi(k/N-x)}.
 \tag{10}
\]
For the second equality, reflection also yields
\[
 G_N(Nx)G_N(-Nx)=\frac{N\sin\pi x}{\sin\pi Nx}.
\]
The finite sine product converts (10) to (7), including
the sign \((-1)^{D+j}\). These are meromorphic identities
first proved off their divisors, and then continued through
their removable values.

Write \(g_N'=G_N'/G_N\). Differentiating (4) gives
\[
 \left.\partial_t B_N(x,t)\right|_{t=\tau_j}
 =-\frac N{2\pi}V_j(x)
   \{g_N'(D-j-Nx)-g_N'(j-Nx)\}.
\]
There are exactly \(D-2j\) recurrence steps between these
two arguments. Logarithmic differentiation of (3) therefore
gives (8). The denominator of each cotangent is, up to sign,
one of the sine factors in the second product in (7).
Multiplying it out leaves one cosine and \(D-1\) sines.
Consequently (8) is entire and has the same band (9).
The statement for (7) follows directly from its \(D\) sine
factors. At the simple node the sum is empty, consistently
with the even angular dependence; no additional derivative
condition is imposed there. \(\square\)

## 3. A canonical entire interpolation

Define the entire cardinal function
\[
 s_N(x)=\frac{\sin\pi Nx}{N\sin\pi x}
       =\frac1N\sum_{k=0}^D e^{2\pi i(k-D/2)x},
 \tag{11}
\]
where the quotient is interpreted by its removable values.
Define an ordinary polynomial in \(z\) by
\[
 \widetilde B_N(x,z)=
       \sum_{i=0}^D s_N(x-i/N)e_i(z).
 \tag{12}
\]
It has degree at most \(D\) in \(z\), and the band (9)
in \(x\).

**Theorem 2.** The class of \(B_N(x,t)\), with
\(z=-2\cos t\), in the full algebra \(\mathcal A_N\)
is exactly the class represented by (12). In particular,
\[
 [B_N(x+1,\cdot)]=\eta[B_N(x,\cdot)]
       \quad\hbox{in }\mathcal A_N.
 \tag{13}
\]
This equality includes the first normal derivatives at every
double root.

**Proof.** The spectral values and derivatives of (4) belong
to the band (9), by Lemma 1. Taking the unique Hermite
representative of degree less than \(N\) is a fixed linear
map, independent of \(x\), so the resulting
\(\mathcal A_N\)-valued function has that same band.

At the \(N\) points \(x=i/N\), (5) specifies its class
as \(e_i\). The cardinal functions in (11) satisfy
\(s_N((i-j)/N)=\delta_{ij}\) for \(0\le i,j<N\).
The \(N\) frequencies (9) have an invertible discrete
Fourier evaluation matrix at these points. Thus (12) is
the unique function with that band and those values.
Equation (13) follows since every frequency in (9) has
the same multiplier \(e^{-\pi iD}=\eta\).
\(\square\)

There is also a direct check of the periodicity. Away from
removable divisors, the factorial period gives
\[
 \frac{B_N(x+1,t)}{B_N(x,t)}
 =\frac{\cos Nt-\eta\cos(2\pi Nx)}{2\sin^2\pi Nx}.
 \tag{14}
\]
At the physical values, \(\cos N\tau_j=\eta\) and
\(\sin N\tau_j=0\). The multiplier is therefore
\(\eta\), and its first angular derivative vanishes.
This verifies (13) at both the value and normal levels.
It would be insufficient to check only its values.

## 4. Exact integration of a paired index

**Theorem 3.** Let \(p(x),q(x)\) be functions with band
(9), valued in any fixed finite-dimensional complex algebra.
Their product is taken in its specified order. Let
\(\Lambda\) be any linear map out of that algebra. Then,
for every real \(a,h\),
\[
 \sum_{i=0}^{N-1}\Lambda(p(i/N)q(i/N))
 =N\int_a^{a+1}\Lambda(p(x+ih)q(x+ih))\,dx.
 \tag{15}
\]
Either factor can be replaced by its reflection
\(p(D/N-x)\), without changing the conclusion.

**Proof.** The product has integer frequencies
\(-D,-D+1,\ldots,D\). Since \(D=N-1\), its grid
average and its period integral both extract exactly its
constant coefficient. Translating the height multiplies
each frequency by a scalar and leaves the constant one
unchanged. Reflection preserves the band. Linearity
proves the assertion with \(\Lambda\). \(\square\)

The theorem applies simultaneously to any finite collection
of independent indices, each occurring in exactly two factors
of band (9). Finite sums and integrals can be interchanged.
An original crossing power at a vertex is an element of its
pair algebra independent of these indices and does not change
their bands. The original closing functional is linear on
that algebra and retains its Hermite data.

For each such index all extra lattice contours vanish
exactly. The side difference is zero by period one. The
upper correction cannot have a constant Fourier coefficient,
since it shifts every frequency upward by at least \(N\).
For the complete lower correction, put \(w=e^{-2\pi ix}\).
The function \(w^Np(x)q(x)\) has a zero of order at least
\(N-D=1\) at zero. The full correction form has the factor
\(w^Np(x)q(x)/(w(1-w^N))\,dw\), which is holomorphic
inside every circle of radius less than one. Its integral
is zero. This retains all Fourier modes, not just the first.

## 5. Boundary parameters and the limit of the assertion

Equation (12) is a literal polynomial identity at the index
grid for every free \(z\). Thus it can be used at open
boundaries too, and (15) still preserves the entire original
boundary polynomial. However, Theorem 2 identifies the
factorial continuation (4) with (12) only in the quotient
\(\mathcal A_N\). At a genuinely free spectral parameter
they need not be equal. Replacing (12) by (4) there requires
a separate estimate or an exact remainder formula.

Likewise, an exact circle representation does not identify
its geometric stationary point or prove a nonzero leading
coefficient. The physical angle contractions remain. The
useful conclusion is that internal paired indices have no
independent lattice-side or Fourier-correction obstruction
after their full spectral data have been retained. The
subsequent contour and growth problem is an angle problem,
with the original boundary polynomial still specified.

## 6. Finite checks

The proof above is algebraic. The accompanying
[reproduction script](../experiments/check_newton_finite_fourier_band.py)
also compares (12) with the canonical factorial formula evaluated
directly from its exact cyclic expression. It constructs the values
and derivatives of the original polynomials (2) by ordinary product
differentiation, so the first-normal comparison does not assume (8).
It checks both the turn pairing and the reflected identity pairing.

Run

~~~sh
python3 experiments/check_newton_finite_fourier_band.py --output repro/results/research-newton-finite-fourier-band.json
~~~

The [saved record](../repro/results/research-newton-finite-fourier-band.json)
covers levels two through twelve at 90 decimal digits, including
both parities and composite levels. These are normalization checks
for the exact identities; they are not evidence for a volume
asymptotic beyond the theorem's stated scope.
