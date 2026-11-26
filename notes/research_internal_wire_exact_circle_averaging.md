# Exact circle averaging for internal Newton wires

Restoring the original Frobenius traces gives a general identity for internal wire indices. Each wire occurs in two Newton factors. In the full quotient algebra, the canonical factorial interpolation of either factor has exactly \(N\) half-integer Fourier frequencies. Their product has integer frequencies between \(-(N-1)\) and \(N-1\). Consequently its complete \(N\)-point sum is exactly its constant Fourier coefficient multiplied by \(N\).

This statement applies to arbitrary finite networks of the original identity and reversal kernels, with arbitrary vertex weights in the quotient algebra. It retains the first normal derivatives at repeated roots. It is an exact transformation of the source, not a volume estimate or a proof of a surviving geometric contribution.

## 1. The full quotient and the interpolation

Fix \(N\ge2\), put \(D=N-1\), and let
\[
 P_N(z)=\prod_{j=0}^{D}\left(z-2\cos\frac{(2j+1)\pi}{N}\right),
 \qquad {\cal A}_N=\mathbb C[z]/(P_N).
\]
The original trace is
\[
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f.
\]
The roots of \(P_N\) have multiplicity two, except for the simple root \(-2\) when \(N\) is odd. Thus an analytic representative defines an element of \({\cal A}_N\) by its values and first derivatives at the double roots, together with the value at that simple root.

For \(0\le j<N\), the Newton polynomials are
\[
 e_j(z)=S_j^{-2}\prod_{k=0}^{j-1}
 \left(2\cos\frac{(2k+1)\pi}{N}-z\right).
\]
Let \(G_N\) be the normalized canonical sine factorial. For \(z=-2\cos t\), set
\[
 {\cal B}_N(x,t)=
 \frac{G_N(D/2+Nt/(2\pi))G_N(D/2-Nt/(2\pi))}
 {G_N(D/2-Nx+Nt/(2\pi))G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
                                                               \tag{1}
\]
At \(x=j/N\), this is exactly \(e_j(-2\cos t)\). Interpret its class
\(\mathbf B_N(x)\in{\cal A}_N\) through the full jets just specified.

Put \(\eta=(-1)^D\). The exact sine recurrence gives
\[
 {\cal B}_N(x+1,t)=
 \frac{\cos Nt-\eta\cos(2\pi Nx)}{2\sin^2(\pi Nx)}
                         {\cal B}_N(x,t).           \tag{2}
\]
The Chebyshev identity, including its leading coefficient, is
\[
 \cos Nt-\eta=\frac{(-1)^N}{2}P_N(-2\cos t).         \tag{3}
\]
Hence in the full quotient,
\[
                   \mathbf B_N(x+1)=\eta\mathbf B_N(x).          \tag{4}
\]
Equation (3) vanishes to the required order at every root. In particular this is not merely an identity at the distinct roots.

## 2. Entire continuation and the Fourier band

**Lemma.** The quotient-valued function \(\mathbf B_N(x)\) is entire and has the expansion
\[
 \mathbf B_N(x)=\sum_{\ell\in\Lambda_N}
          \mathbf c_{N,\ell}e^{2\pi i\ell x},
 \qquad
 \Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}.              \tag{5}
\]
Its coefficients are exactly
\[
 \mathbf c_{N,\ell}=\frac1N\sum_{j=0}^{D}
           e_j\,e^{-2\pi i\ell j/N}.                \tag{6}
\]

The [direct sine-product proof](research_newton_interpolation_finite_fourier_band.md) establishes this statement explicitly at every spectral value and first normal, without a growth argument. The proof below records a second derivation from the exact factorial continuation.

**Proof.** Choose \(0<\theta<1\). The physical angles may be taken in
\([-\pi+\pi/N,\pi-\pi/N]\). For
\(-\theta/N\le\Re x\le1-\theta/N\), the arguments of the two numerator factorials in (1) lie between \(0\) and \(D\). The real parts of its two shifted denominator arguments are strictly less than \(N\); their maximum is \(D+\theta<N\). Reciprocals of \(G_N\) have no poles there. The remaining denominator has \(-1<\Re(Nx)<N\) and is nonzero. These inequalities persist on neighborhoods of the spectral angles and on a slightly wider \(x\)-strip. All required spectral jets of (1) are consequently holomorphic there. Equation (4) continues them to the entire plane.

At a double root, a value and one \(z\)-derivative are required. Away from \(t=0\), this is a value and one \(t\)-derivative, since \(dz/dt=2\sin t\ne0\). At the odd-level simple root \(t=0\), only a value is required. No second \(t\)-derivative is introduced at that endpoint.

The exact factorial formula in [the boundary-order calculation](research_balanced_factorial_boundary_order.md) gives quadratic balance for (1), with linear coefficient \(L=D/2\). Its three signed slopes are \(1,-1,-1\), with multiplicities \(-2,-1,-1\). Their quadratic contribution is \(-2+1+1=0\); their linear contribution is
\[
 \frac N2(-D/N)-\frac{N-1}{4}(-4)=D/2.
\]
The small-disk multiplier is identically one at the physical jets, by (2)--(3). The same exact formula therefore gives, for each fixed \(N\) and any norm on the finite-dimensional algebra,
\[
 \|\mathbf B_N(a+ih)\|\le C_N e^{\pi D|h|}
 \quad (a\text{ in a fixed interval},\ |h|\text{ sufficiently large}).
                                                               \tag{7}
\]
The first normal derivatives have the same bound: the linear coefficient \(D/2\) is independent of the spectral parameter, and the defect of the small-disk multiplier from one, together with its first spectral normal, vanishes by (3). Upper growth follows by conjugation of the defining gamma product.

An entire function with period multiplier \(\eta=e^{-\pi iD}\) has Fourier frequencies in \(\mathbb Z-D/2\). Its coefficient at frequency \(\ell\) can be computed on any horizontal period. Moving that period downward in (7) makes the coefficient zero for \(\ell>D/2\); moving it upward makes it zero for \(\ell<-D/2\). This proves (5) componentwise in \({\cal A}_N\). The \(N\) frequencies in \(\Lambda_N\) differ by distinct integers of absolute difference less than \(N\), so their \(N\)-point evaluation matrix is orthogonal after normalization. Since \(\mathbf B_N(j/N)=e_j\), inversion gives (6). \(\square\)

The reflected interpolation \(\mathbf B_N(D/N-x)\) has the same band and the same period multiplier. Its coefficients acquire the explicit factors \(e^{2\pi i\ell D/N}\), with reversed frequency.

There is a useful domain distinction. Over all continuous angles \(t\in[-\pi,\pi]\), avoiding the corner poles of the unreflected factorial ratio would require \(\theta<1/2\), whereas the reflected ratio would require \(\theta>1/2\). A common choice does not exist. The physical spectral jets have the larger margin used above, so every \(0<\theta<1\) works for both orientations. The lemma is proved at those full jets before any continuous-angle deformation.

## 3. The network theorem

Let a finite network have a copy of \({\cal A}_N\) at each traced vertex. Put any weight \(W_v\in{\cal A}_N\) at vertex \(v\). Original twist weights, including negative powers when defined, are permitted. Each internal edge has one of the two kernels
\[
 K_I(z,w)=\sum_{j=0}^{D}e_j(z)e_{D-j}(w),
 \qquad
 K_T(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w).
\]
At each vertex multiply its incident factors and its weight, then apply the original \(\phi_N\). Boundary factors and their finite index sums may be left unchanged.

For every internal edge \(e\), replace its two Newton factors by
\(\mathbf B_N(x_e)\) or \(\mathbf B_N(D/N-x_e)\), according to the actual orientation. Perform the same vertex products and traces. Call the resulting function \({\cal F}_N(\mathbf x;\mathbf u)\), where \(\mathbf u\) denotes all untraced boundary data.

**Theorem.** If \(E_{\mathrm{int}}\) is the set of internal edges, then
\[
 \boxed{
 \sum_{\mathbf j\in\{0,\ldots,D\}^{E_{\mathrm{int}}}}
 {\cal F}_N(\mathbf j/N;\mathbf u)
 =
 N^{|E_{\mathrm{int}}|}
 \int_{\mathbf a+[0,1]^{E_{\mathrm{int}}}+i\mathbf h}
             {\cal F}_N(\mathbf x;\mathbf u)\,d\mathbf x.}
                                                               \tag{8}
\]
Every \(\mathbf a,\mathbf h\in\mathbb R^{E_{\mathrm{int}}}\) is allowed.
The identity holds at every integer level and as an identity in the full boundary polynomial, with all its derivatives.

**Proof.** Each internal index occurs in exactly two factors. By (5), its frequencies are sums of two members of \(\Lambda_N\), hence are integers in \([-D,D]\). Reversal does not change this interval. Vertex multiplication, arbitrary vertex weights, and the linear trace cannot enlarge the band in that index. This remains true for loops, where both factors are at the same traced vertex.

For any integer frequency \(m\) with \(|m|\le D<N\),
\[
 \frac1N\sum_{j=0}^{N-1}e^{2\pi imj/N}
       =\mathbf1_{m=0}
       =\int_{a+ih}^{a+1+ih}e^{2\pi imx}\,dx.
\]
Apply this identity to each internal index of the finite Fourier expansion. All operations are finite, and the original boundary operations are unchanged. This proves (8). \(\square\)

Thus no internal-index alias, endpoint current, or first-normal correction is omitted: in this representation their total is exactly zero. There is no asymptotic error to control in (8).

## 4. A quantitative finite-band bound

For any norm on \({\cal A}_N\), (6) implies
\[
 \|\mathbf c_{N,\ell}\|
 \le\frac1N\sum_{j=0}^{D}\|e_j\|,
 \qquad
 \|\mathbf B_N(a+ih)\|
 \le e^{\pi D|h|}\sum_{j=0}^{D}\|e_j\|.             \tag{9}
\]
The same holds for the reflected function, since its extra frequency factors have modulus one. Products, the explicit multiplication norm of the finite algebra, and the norms of the given trace functionals give a finite, computable bound for any network integrand on its shifted torus. These bounds are exact finite-dimensional estimates. Their exponential rates need not equal the hyperbolic volume, and (9) does not assert that they do.

The theorem is closed under arbitrary gluing of internal identity and reversal wires: each newly internal wire still has precisely two half-band factors. This is stronger than a single-coordinate small-circle estimate. It applies to every fixed finite traced network independently of vertex degree and twist size.

## 5. What remains at free boundaries and in the volume problem

An untraced boundary angle does not impose \(P_N(z)=0\). For that factor the difference in (3) survives, and its gamma interpolation is not covered by (5). Consequently the exact Gamma-circle theorem applies to internal wires. Boundary indices can remain in their original finite sums, yielding the full boundary-polynomial identity (8).

One may instead use the entire cardinal interpolation
\[
 \widetilde{\cal B}_N(x,z)
 =\sum_{\ell\in\Lambda_N}\left(
       \frac1N\sum_{j=0}^{D}e_j(z)e^{-2\pi i\ell j/N}
                         \right)e^{2\pi i\ell x}
\]
at every free end as well. Then all paired wires have the same exact averaging identity. This interpolation equals (1) in the quotient, but not in general at a free \(z\). Its asymptotic phase cannot be imported from (1) without a separate argument.

Finally, (8) reorganizes the exact state. It does not locate a geometric critical point, establish a global phase loss, or prove a nonzero selected contribution. Those remain analytic and geometric tasks for the restored network. The gain is a general removal of the internal-index lattice problem, without a knot-by-knot contour calculation.
