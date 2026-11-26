# The original cyclic dilogarithm near the unit circle

24 November 2026. Written research proof.

The norm-one cyclic dilogarithm in the original knot period has a
uniform logarithmic estimate through the unit circle. Polynomial
separation from its root divisors gives a logarithmic error. At closer
approaches an explicit root factor gives the same error, even when
the distance is superexponentially small in the level. All factors
belong to the actual function; no closed-period lower bound is inferred.

## 1. The actual atom and the estimate

Put \(N\ge2\), \(Q=e^{2\pi i/N}\), and
\(\mu_N=\{Q^j:0\le j<N\}\). Use C's unchanged functions
\[
 D_N(t)=\prod_{j=1}^{N-1}(1-Q^jt)^{j/N},\qquad
 V_N(t)=\frac{(1-t^N)^{(N-1)/(2N)}}{D_N(t)},\qquad
 U_N(t)=V_N(t)^{-1}.                                      \tag{1}
\]
All branches start at one at zero and are continued along the specified
path avoiding \(\mu_N\). Their moduli are independent of that path,
since every exponent in (1) is real. Define the continuous function
\[
 F(t)=\begin{cases}
 \operatorname{Im}\operatorname{Li}_2(t)/(2\pi),&0<|t|\le1,\\
 -\operatorname{Im}\operatorname{Li}_2(1/t)/(2\pi),&|t|>1.
 \end{cases}                                               \tag{2}
\]
Here \(\operatorname{Li}_2(z)=\sum_{m\ge1}z^m/m^2\) on the closed
unit disk. Its continuity and conjugation symmetry show that the two
boundary values in (2) agree.

Write \(\zeta_j=Q^{-j}\), \(\beta_j=(N-1-2j)/(2N)\), and
\(\delta=\operatorname{dist}(t,\mu_N)\). For \(t\notin\mu_N\), put
\[
 B_N(t)=\begin{cases}
 \beta_j\log(N|t-\zeta_j|),&|t-\zeta_j|<1/N,\\
 0,&\delta\ge1/N.
 \end{cases}
\]
The first case has at most one index, because distinct roots are
separated by at least \(4/N\).

**Theorem.** Fix \(R\ge1\). Uniformly for all \(N\ge2\) and
\(R^{-1}\le|t|\le R\), \(t\notin\mu_N\),
\[
 \left|\log|V_N(t)|-NF(t)-B_N(t)\right|\le C_R\log N,
 \quad
 \left|\log|U_N(t)|+NF(t)+B_N(t)\right|\le C_R\log N.        \tag{3}
\]
Consequently, for every fixed \(A>0\),
\[
 \operatorname{dist}(t,\mu_N)\ge N^{-A}
 \quad\Longrightarrow\quad
 \left|\log|V_N(t)|-NF(t)\right|\le C_{A,R}\log N.            \tag{4}
\]
The inverse has the same assertion with leading term \(-NF\).
These statements allow arbitrary level-dependent arguments satisfying
the displayed conditions.

## 2. A weighted logarithmic sum away from the root disks

For this section suppose \(\delta\ge1/N\). Write \(t=re^{i\theta}\),
\(g_t(u)=\log|1-te^{2\pi iu}|\), and
\(I(t)=\int_0^1u g_t(u)\,du\), using the ordinary improper integral
when \(r=1\). Let \(u_0=-\theta/(2\pi)\) modulo one, and let
\(d(u,u_0)\in[0,1/2]\) denote circular distance. Exactly
\[
 |1-te^{2\pi iu}|^2=(1-r)^2+4r\sin^2\!\bigl(\pi(u-u_0)\bigr).
                                                               \tag{5}
\]
On the stated annulus, almost everywhere,
\[
 |g_t(u)|\le C_R+|\log d(u,u_0)|,\qquad
 \int_0^1|g_t(u)|\,du\le C_R.
\]
Indeed the modulus is at most \(1+R\) and at least
\(2\sqrt r|\sin\pi(u-u_0)|\ge4R^{-1/2}d(u,u_0)\).
Where \(d>0\), differentiation also gives
\[
 |g_t'(u)|\le\pi|\cot\pi(u-u_0)|\le C/d(u,u_0).             \tag{6}
\]

Partition \([0,1]\) into \(I_j=[j/N,(j+1)/N]\), and put
\(w_j=j/N\). Mark as exceptional every cell meeting the circular
\(2/N\)-neighborhood of \(u_0\). There are at most eight, including
when this neighborhood crosses the seam at zero and one.
Every sample satisfies \(g_t(j/N)=\log|t-Q^{-j}|\ge-\log N\),
and its upper bound depends only on \(R\). On an interval of length
\(h\le1/2\), the integral of \(|\log d(u,u_0)|\) is at most
\(Ch\log(e/h)\), uniformly in its position; split at the seam if needed.
Thus \(N\int_{I_j}|g_t|\le C_R+C\log N\), and all exceptional
sample-versus-average errors total \(O_R(\log N)\).

On the remaining cells, the sum of the oscillations is at most
\(\int|g_t'|\) over those cells. By (6) this is \(O(\log N)\),
as their distance from \(u_0\) is at least \(2/N\). Consequently
\[
 \sum_{j=0}^{N-1}w_j\left(g_t(j/N)-N\int_{I_j}g_t(u)\,du\right)
                                      =O_R(\log N).
\]
Replacing \(w_j\) by \(u\) in the integrals costs at most
\(\int_0^1|g_t|\le C_R\), since \(|w_j-u|\le1/N\). Hence
\[
 \sum_{j=1}^{N-1}\frac jN\log|1-Q^jt|
                            =NI(t)+O_R(\log N).             \tag{7}
\]
This treats the weight's seam explicitly, without extending \(u\)
periodically.

## 3. The central norm and the two chambers

For every nonzero \(t\), with \(\delta=\operatorname{dist}(t,\mu_N)\),
there is an absolute \(c>0\) such that
\[
 c\min(1,N\delta)\le
 \frac{|1-t^N|}{\max(1,|t|^N)}\le2.                          \tag{8}
\]
Choose the nearest root in angle and write
\(t=rQ^ke^{i\varphi}\), \(|\varphi|\le\pi/N\). Put
\(a=N|\log r|\), \(b=N\varphi\). The squared ratio in (8) is
\((1-e^{-a})^2+4e^{-a}\sin^2(b/2)\). If \(a\ge1\), it has a
fixed positive lower bound. If \(a\le1\), its square root is at
least \(c\sqrt{a^2+b^2}\), while
\(|r e^{i\varphi}-1|\le C\sqrt{a^2+b^2}/N\).
The chosen root is also nearest in Euclidean distance. This proves
the lower bound; the upper bound is the triangle inequality.

When \(\delta\ge1/N\), (8) gives
\(\log|1-t^N|=N\log^+|t|+O(1)\). Thus (1),(7) imply
\[
 \log|V_N(t)|=
 N\left(\tfrac12\log^+|t|-I(t)\right)+O_R(\log N).           \tag{9}
\]
The remaining term \(-\tfrac12\log^+|t|\) is bounded on the annulus.
The central norm factor itself has not been omitted.

For \(|t|<1\), integrating the absolutely convergent logarithmic
series, with \(\int_0^1u e^{2\pi imu}du=1/(2\pi im)\), gives
\(I(t)=-\operatorname{Im}\operatorname{Li}_2(t)/(2\pi)\).
For \(|t|>1\), write
\(g_t(u)=\log|t|+\log|1-t^{-1}e^{-2\pi iu}|\); then
\(I(t)=\tfrac12\log|t|+\operatorname{Im}\operatorname{Li}_2(1/t)/(2\pi)\).
The uniform small-interval integral bound following (5), together
with continuity away from the singular angle, proves continuity
of these integrals at the unit circle. Equation (9) therefore
proves (3) outside the root disks.

There is also an exact modulus identity:
\[
 |V_N(t)V_N(1/t)|=\frac{|1-t|}{|1-t^N|^{1/N}}.               \tag{10}
\]
Indeed reindexing \(j\mapsto N-j\) gives
\(|D_N(t)D_N(1/t)|=|t|^{-(N-1)/2}|1-t^N|/|1-t|\).
The numerator norm factors in (1) give (10). This identity is
understood off \(\mu_N\), without resetting any branch.

## 4. Uniform estimates inside every root disk

Factoring \(1-t^N\), with the same anchor at zero, gives exactly
\[
 V_N(t)=\prod_{k=0}^{N-1}(1-Q^kt)^{\beta_k},\qquad
 W_{N,j}(t):=V_N(t)(1-Q^jt)^{-\beta_j}
              =\prod_{k\ne j}(1-Q^kt)^{\beta_k}.             \tag{11}
\]
Every continued branch of \(W_{N,j}\) extends holomorphically and
without zeros to \(|t-\zeta_j|<1/N\). Its modulus at the center is
\[
 |W_{N,j}(\zeta_j)|=|(Q;Q)_j|\,N^{-(j+1/2)/N},
 \qquad (Q;Q)_0=1.                                        \tag{12}
\]
For a direct verification put \(L_l=\log|1-Q^l|\). The product
of the nontrivial roots gives \(\sum_{l=1}^{N-1}L_l=\log N\),
and symmetry gives \(\sum lL_l=(N/2)\log N\). Reindexing
\(k=j+l\) modulo \(N\) in (11) yields
\[
 \log|W_{N,j}(\zeta_j)|
 =\left(\frac{N-1}{2N}-\frac jN-\frac12\right)\log N
       +\sum_{l=N-j}^{N-1}L_l,
\]
which is (12), including the empty sum at \(j=0\).

Let \(s=\min(|k-j|,N-|k-j|)\ge1\). On the disk,
\(|t-\zeta_k|\ge(4s-1)/N\), because
\(2\sin(\pi s/N)\ge4s/N\). Since \(|\beta_k|\le1/2\),
\(|(\log W_{N,j})'(t)|\le CN\log N\).
Integrating along the straight segment from the center changes
\(\log|W_{N,j}|\) by at most \(C\log N\).

Here is the endpoint-aware factorial estimate needed in (12).
Set \(J(v)=\int_0^v\log(2\sin\pi u)\,du\). Uniformly for
\(0\le j<N\),
\(\log|(Q;Q)_j|=NJ(j/N)+O(\log N)\).
To prove it, split
\(\log(2\sin\pi u)=\log u+\log(1-u)+h(u)\), where \(h\)
extends smoothly to \([0,1]\). The right Riemann sums for the two
monotone logarithms differ from their integrals by \(O(\log N)\),
including the first cell of \(\log u\) and the final allowed sample
\(j=N-1\). The smooth remainder costs \(O(1)\). The case \(j=0\)
is exact. Differentiating the boundary dilogarithm and using its
value at one gives \(J(v)=F(e^{-2\pi iv})\). Therefore
\[
 \left|\log|W_{N,j}(t)|-NF(\zeta_j)\right|\le C\log N
 \qquad (|t-\zeta_j|<1/N),                                \tag{13}
\]
including the center itself.

For \(|z|,|w|\le1\), \(d=|z-w|\le1/2\), the series estimate
\(|z^m-w^m|\le\min(md,2)\) gives
\(|\operatorname{Li}_2(z)-\operatorname{Li}_2(w)|
 \le Cd\log(e/d)\). Apply it directly inside the unit disk and
to \(1/t,1/\zeta_j\) outside. If \(\delta=|t-\zeta_j|<1/N\),
then \(N|F(t)-F(\zeta_j)|\le C\log N\).
Combining (11),(13), and \(|\beta_j|\le1/2\) proves (3) inside
the root disk, with \(\beta_j\log(N\delta)\) retained.
Inversion proves the assertion for \(U_N\). If additionally
\(\delta\ge N^{-A}\), this root correction has magnitude at most
\(\tfrac12\max(A-1,0)\log N\), proving (4).

## 5. Sharp envelope and scope

Put \(v_3=\operatorname{Im}\operatorname{Li}_2(e^{\pi i/3})\),
the volume of a regular ideal tetrahedron. Harmonicity and boundary
continuity reduce the disk extrema to the unit circle. There the
angular derivative is \(-\log|2\sin(\theta/2)|\), so the maximum
is \(v_3\) at \(\theta=\pi/3\), and the minimum is \(-v_3\) at
\(5\pi/3\). Formula (2) gives the same bounds outside. Consequently
\[
 |V_N(t)|\le N^{C_R}e^{Nv_3/(2\pi)+B_N(t)},\qquad
 |U_N(t)|\le N^{C_R}e^{Nv_3/(2\pi)-B_N(t)}.                 \tag{14}
\]
Under polynomial root separation, the correction is absorbed in a
power of \(N\). At closer approaches its original exponent is mandatory.

H already gives the sharp per-atom constant \(v_3/(2\pi)\), and
S gives the two chamber actions and exact resonant source values.
The refinement is uniform control near the circle, including the
regularized functions throughout every root disk. It does not reduce
the number of atoms in an actual word or replace H's endpoint integrals.
No unrestricted finite value of the unregularized atom is assigned at
its roots. C's source, inverse atoms, reflected monomials, Gaussian
weights, Cauchy factors and external scalar remain unchanged.
These function estimates neither bound a coherent contraction below
nor transport its selected geometric cycle.

## Complete input and coverage

| Key | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| C | [Actual continuous source](actual_continuous_gaussian_cyclic_network.md) | 378 | ee47ebbb53258d84ded684e22b1bdfaf193b7fa9a3c852889bf86cb99eb6930c |
| H | [Actual cut cycle and endpoint envelope](actual_cyclic_dilog_hankel_cycle.md) | 316 | 502ddfc4b13c7bd775bf27398592085f3951019ff959e1fe6e363a1a468993ea |
| S | [Earlier chamber actions and resonant source flags](cyclic_source_connection_and_resonant_flags.md) | 401 | cdb07713bec8bd0b45b1a36a9676d2f1bb890b842c7d85d947cfa7e978c2d7b3 |

C is the sole complete selected proof input; H and S are complete
coverage. All estimates are proved directly. Only written mathematics
and text/hash operations were used. Earlier finals, public manuscripts
and the progress ledger remain unchanged.
