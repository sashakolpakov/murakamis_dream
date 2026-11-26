# Partial-wire boundary observations recover the full original source

Private written proof, 17 November 2026.

The original cardinal halfwire has a finite family of real partial-period
observations which determines every Newton coefficient, including the
repeated-root normal data. The reconstruction has polynomial condition
bounds. Its complete period alone retains just one coefficient. This
distinction is relevant to a partial wire-side current: replacing that
current by its completed-period observation loses actual source data.

The result uses the original trace, the fixed left state \(1\), and the
original wire normalization. It does not give a lower bound for any one
prescribed closed scalar, or a bound after moving the observations to a
fixed complex height.

## 1. The actual source and its complete period

Fix \(N\ge2\), \(D=N-1\), and use the original algebra and normalization
from the complete compiler C:
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi(e_i e_j)=\delta_{i+j,D},\qquad e_0=1.
 \tag{1}
\]
Its Newton basis and spectral nodes are
\[
 e_j(z)=S_j^{-2}\prod_{a=0}^{j-1}(c_a-z),\quad
 c_a=2\cos\frac{(2a+1)\pi}{N},\quad
 S_j=\prod_{a=1}^j2\sin\frac{\pi a}{N}.
 \tag{2}
\]
Thus the coefficients of a class in this basis retain all its full
Hermite data, not just its values at distinct nodes.

The exact original cardinal representative in S(10) is
\[
 \widetilde B_N(x,z)=\sum_{j=0}^D C_j(x)e_j(z),\qquad
 C_j(x)=\frac{\sin\pi N(x-j/N)}{N\sin\pi(x-j/N)}
       =\frac1N\sum_{\nu\in\Lambda_N}e^{2\pi i\nu(x-j/N)},
 \quad
 \Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}.
 \tag{3}
\]
All apparent singularities of \(C_j\) are removable. The functions are
periodic for odd \(N\) and antiperiodic for even \(N\); products of two
have integer Fourier frequencies in \([-D,D]\). The source S identifies
(3) with the full Hermite data of the original factorial halfwire. C
retains the same representative at a free ordinary polynomial boundary.

Let \(E=\sum_{r=0}^D a_r(E)e_r\) be an arbitrary original full class,
independent of the opened wire coordinate \(x\). It can depend on any
other fixed or free parameters. Keep the actual left state \(p=e_0=1\)
and define the fully traced wire density and its normalized primitive by
\[
 \begin{split}
 F_E(x)&=\phi_z\phi_w\bigl[
       p(z)E(w)\widetilde B_N(x,z)\widetilde B_N(x,w)\bigr],\\
 B_E(x)&=N\int_0^x F_E(s)\,ds .
 \end{split}
 \tag{4}
\]
The integral is the entire primitive based at zero. The factor \(N\)
is the original wire factor in S(15), rather than a normalization chosen
for the estimates below. Directly from (1),
\[
 F_E(x)=C_D(x)g_E(x),\qquad
 g_E(x)=\sum_{j=0}^D a_{D-j}(E)C_j(x).
 \tag{5}
\]
For real \(x\) the cardinals are real. Their finite frequency formula
gives both the Hermitian and bilinear identities
\[
 \int_0^1 C_j(x)\overline{C_k(x)}\,dx
 =\int_0^1 C_j(x)C_k(x)\,dx=\frac{\delta_{jk}}N.
 \tag{6}
\]
Indeed frequency differences are integers, and the surviving finite
sum is the \(N\)-point Fourier sum. In the bilinear version the surviving
frequencies are opposite. Consequently
\[
                  B_E(1)=a_0(E)=E(c_0).
 \tag{7}
\]
This is also the original identity
\(\phi_z\phi_w[p(z)E(w)K_T(z,w)]=E(c_0)\), since
\(K_T=\sum_j e_j\otimes e_j\). The two descriptions have the same
orientation and scalar.

## 2. A polynomially conditioned partial-current frame

Put \(x_k=(k+1/2)/N\), \(0\le k\le D\), and set
\(M_{kj}=C_j(x_k)\). Then \(M\) is unitary at both parities. To see this,
write
\[
 M=UV^*,\qquad
 U_{k\nu}=N^{-1/2}e^{2\pi i\nu x_k},\qquad
 V_{j\nu}=N^{-1/2}e^{2\pi i\nu j/N}.
 \tag{8}
\]
Both \(U\) and \(V\) are unitary: the difference of two frequencies in
\(\Lambda_N\) is an integer of magnitude less than \(N\). This argument
includes the half-integer frequencies at even levels.

At these midpoints,
\[
 |C_D(x_k)|=
 \frac1{N\left|\sin\bigl(\pi(k+1/2-D)/N\bigr)\right|},
 \qquad \frac1N\le |C_D(x_k)|\le1.
 \tag{9}
\]
The numerator of the sine quotient has modulus one. Its lower bound
uses \(|\sin|\le1\); the upper bound follows directly from the sum of
\(N\) unit-modulus terms in (3).

**Theorem 1.** The \(N\) actual partial-current derivatives
\(B'_E(x_k)\) determine the entire original class \(E\), with
\[
 \boxed{\quad
 \sum_{r=0}^D|a_r(E)|^2
 \le\sum_{k=0}^D|B'_E(x_k)|^2
 \le N^2\sum_{r=0}^D|a_r(E)|^2 .\quad}
 \tag{10}
\]
Their inverse is explicit:
\[
 a_r(E)=\frac1N\sum_{k=0}^D
       \overline{C_{D-r}(x_k)}\,
                  \frac{B'_E(x_k)}{C_D(x_k)}.
 \tag{11}
\]

**Proof.** Let \(J\) reverse the coefficient vector. Equations (4)--(5)
give
\[
 (B'_E(x_k))_k=N\operatorname{diag}(C_D(x_k))\,MJa(E).
 \tag{12}
\]
Use (8)--(9) for (10), and invert this product for (11). No Hermitian
adjoint replaces the original bilinear trace: conjugation in (11) is
only the inverse of the numerical unitary matrix \(M\). \(\square\)

In particular the singular values of the observation matrix lie in
\([1,N]\). The estimate is uniform over arbitrary \(N\)-dependent
classes \(E\). All exterior-parameter derivatives satisfy the same
identities, applied to their coefficient vectors. The theorem recovers
every physical normal because the entire full-algebra coefficient
vector is recovered.
In particular, if these observations factor through a linear quotient
of the full source space, that quotient must be injective by (10) and
must have dimension at least \(N\).

## 3. Partial-period values alone suffice

Write \(a_0=B_E(1)\) and
\[
 P_E(x)=B_E(x)-a_0x,\qquad y_\ell=\frac{\ell}{2N},
                 \quad 0\le\ell<2N.
 \tag{13}
\]
The product in (5) has integer frequencies in \([-D,D]\), and its
normalized mean is \(a_0\). Therefore \(P_E\) is a periodic
trigonometric polynomial with frequencies in \([-D,D]\), anchored by
\(P_E(0)=0\). Its constant coefficient need not vanish.

Its \(2N\) sample values determine it without aliases:
\[
 \widehat P_m=\frac1{2N}\sum_{\ell=0}^{2N-1}
      P_E(y_\ell)e^{-2\pi im y_\ell},\qquad |m|\le D,
 \quad
 P_E(x)=\sum_{m=-D}^D\widehat P_m e^{2\pi imx}.
 \tag{14}
\]
Indeed distinct frequencies in this range differ by less than \(2N\).
Thus the actual values \(B_E(y_\ell)\), together with the actual complete
period \(B_E(1)\), give \(B'_E\), and (11) reconstructs \(E\).

These endpoint observations also have polynomial condition bounds.
Put
\[
 \mathcal D_N(E)^2=N|a_0|^2+
                     \sum_{\ell=0}^{2N-1}|P_E(y_\ell)|^2.
 \tag{15}
\]
Discrete Parseval and (14) give
\[
 \sum_{\ell=0}^{2N-1}|P'_E(y_\ell)|^2
       \le(2\pi D)^2\sum_{\ell=0}^{2N-1}|P_E(y_\ell)|^2.
\]
The midpoint grid is the odd subgrid of \(y_\ell\). Combining this
estimate with \(|a_0+P'_E|^2\le2|a_0|^2+2|P'_E|^2\) and (10) proves
\[
 \|a(E)\|_2^2\le
 8\pi^2D^2\sum_\ell|P_E(y_\ell)|^2+2N|a_0|^2
 \le8\pi^2D^2\mathcal D_N(E)^2.
 \tag{16}
\]
Conversely, (6) gives \(\|g_E\|_{L^2(0,1)}^2=\|a(E)\|_2^2/N\).
Since \(|C_D|\le1\) on the real interval,
\(\|B'_E\|_{L^2}^2\le N\|a(E)\|_2^2\). Subtracting its mean reduces
the squared norm, so the same bound holds for \(P'_E\). The anchor
\(P_E(0)=0\) and Cauchy--Schwarz imply
\(\sup_{[0,1]}|P_E|^2\le N\|a(E)\|_2^2\). Hence
\[
       \mathcal D_N(E)^2\le(2N^2+N)\|a(E)\|_2^2.
 \tag{17}
\]
Thus no differentiation of observed data is needed for exact
reconstruction. Equations (14), (11), and (16)--(17) give the finite
reconstruction and polynomial bounds by written identities alone.

## 4. Correlated sources on several opened wires

For fixed \(s\), take an arbitrary joint class
\(E\in\mathcal A_N^{\otimes s}\), independent of the opened wire
coordinates, put \(p=e_0\) on each exposed left
port, and use the product of the actual halfwire pairs. Let
\(B_E(\mathbf x)\) be its rectangular partial primitive, with the
original prefactor \(N^s\). If \(a_{r_1\ldots r_s}\) are its joint
Newton coefficients, the midpoint mixed-derivative observation matrix
is the tensor power of the matrix in (12). Consequently
\[
 \|a(E)\|_2^2\le
 \sum_{\mathbf k\in\{0,\ldots,D\}^s}
 \left|\partial_{x_1}\cdots\partial_{x_s}
              B_E(x_{k_1},\ldots,x_{k_s})\right|^2
 \le N^{2s}\|a(E)\|_2^2.
 \tag{18}
\]
The tensor product of (11) is its exact inverse; the full rectangular
period retains only \(a_{0\ldots0}\). No factorization of \(E\) is
assumed. Arbitrary joint spectators and their ordinary derivatives
remain. The conditioning is polynomial for fixed \(s\), on precisely
this real observation grid.
Any linear quotient retaining all these joint observations therefore
has dimension at least \(N^s\).

## 5. Partial currents do not descend to short physical data

Here is an exact distinction from a low-degree turn estimate. Put
\(m=\lfloor N/2\rfloor\). Define
the short physical data to be all distinct-node values when \(N\) is
odd; when \(N=2m\) is even, use the \(m\) distinct-node values together
with the first derivative at \(c_{m-1}\). These data determine a
polynomial of degree at most \(m\), but for \(N\ge3\) not an arbitrary
full class.

For every \(N\ge3\), the actual class \(E=e_D=\mathsf T1\) has zero
short data. In odd degree, every distinct node occurs among the factors
of (2) for \(e_D\), including the simple node \(-2\). In even degree
\(N\ge4\), both occurrences \(c_{m-1}=c_m\) appear there, so the
central first derivative also vanishes. At \(N=2\) this assertion is
false: the short data are already full and include \(e_1'(0)\ne0\).

Nevertheless (5) gives for \(N\ge3\)
\[
          F_{e_D}(x)=C_D(x)C_0(x)\not\equiv0,
          \qquad B_{e_D}(1)=0.
 \tag{19}
\]
The midpoint observations are nonzero, since both cardinal numerators
have modulus one there. Thus a norm depending only on those short data
cannot bound the full family of partial-current observations. This is
an inserted original source with a literal turn of \(1\); it is not a
claim that an uninserted reduced knot invariant vanishes.

The previously known full-period cardinal identity is the starting
point, not a new result here. The additional conclusion is the exact
finite boundary reconstruction and its condition bounds. Full traces
in (4) make the factorial and cardinal representatives agree, including
their physical normals. On an untraced continuous angular contour,
the factorial-to-cardinal primitive and moving-seam corrections in
S(31)--(32) remain required. The present reconstruction neither deletes
those currents nor estimates a complex partial arc or a geometric
closing. A nonzero family of observations need not make a specified
one of them nonzero. The samples span an entire real wire period;
they are not confined to one geometric window. Finite Fourier
continuation to a fixed nonreal height can have exponential cost in
\(N\), so no polynomial bound for such a continuation is asserted.

## Direct sources

Both complete direct texts were freshly read in full, their used
implications checked, and their hashes renewed before freezing this
proof.

* S: [The original source at a stationary wire escape](research_stationary_wire_escape_current.md),
  SHA256 `03f902ea70818cf8432dd3d947822b49d1f762487552b20dac7e431b8222aa4e`.
  Used: the actual cardinal halfwire, its full-Hermite source meaning,
  original wire normalization, and the retained seam scope.
* C: [Exact source compilation with arbitrary crossing powers](research_arbitrary_power_source_compilation.md),
  SHA256 `55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f`.
  Used: the original Newton algebra, trace, turn, and joint/free-boundary
  source conventions.

Only written mathematics, source-text reads, and file hashes were used.
No mathematical program, numerical computation, test, or build was run.
Frozen manuscripts and other authors' finals were unchanged.
