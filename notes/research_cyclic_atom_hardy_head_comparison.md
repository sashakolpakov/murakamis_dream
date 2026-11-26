# Hardy norms of the cyclic dilogarithm and its finite coefficients

24 November 2026. Written research proof.

The original norm-one cyclic dilogarithm and its inverse belong to
Hardy space. Projecting either symbol to its actual first \(N\) Taylor
coefficients loses at most a power of the level in norm. The same
comparison holds on every concentric disk, uniformly down to radius
zero. This controls scalar symbol norms, with their original phases
and normalizations; it does not estimate a marked word from below.

## 1. The actual functions and their physical heads

Let \(N\ge2\), \(d=N-1\), \(Q=e^{2\pi i/N}\), and
\(F_a=(Q;Q)_a\), \(F_0=1\). Retain the anchored functions of C:
\[
 V_N(z)=(1-z^N)^{(N-1)/(2N)}
             \prod_{j=1}^{N-1}(1-Q^jz)^{-j/N},
 \qquad U_N(z)=V_N(z)^{-1}.                              \tag{1}
\]
They are holomorphic on the open unit disk, with value one at zero.
Use the coefficient Hardy norm
\[
 \|f\|_{H^2}^2=\sum_{a\ge0}|f_a|^2
   =\sup_{0<r<1}\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^2d\theta,
 \qquad f(z)=\sum_{a\ge0}f_a z^a,
\]
and let \(\Pi_N\) be the orthogonal projection to degrees below \(N\).
Then the exact physical scalar heads are
\[
 \Pi_NU_N=u_N(z)=\sum_{a=0}^d\frac{z^a}{F_a},\qquad
 \Pi_NV_N=v_N(z)=\sum_{a=0}^d
       \frac{(-1)^aQ^{a(a-1)/2}z^a}{F_a}.                   \tag{2}
\]
Here is a direct normalization check. Reindexing the product (1),
with all roots anchored at zero, gives
\[
 (1-z)V_N(Qz)=(1-z^N)^{1/N}V_N(z),\qquad
 U_N(Qz)=(1-z)(1-z^N)^{-1/N}U_N(z).
\]
Below degree \(N\), the norm-root factors equal one. The two
coefficient recurrences, initialized by one, are respectively
\((Q^a-1)v_a=Q^{a-1}v_{a-1}\) and
\((Q^a-1)u_a=-u_{a-1}\). These prove (2), including its phases.

**Theorem.** There is a universal \(C\) such that for every \(N\ge2\),
every \(0\le r\le1\), and either pair
\((A_N,p_N)=(V_N,v_N)\) or \((U_N,u_N)\),
\[
 \|p_N(r\,\cdot)\|_{H^2}
 \le\|A_N(r\,\cdot)\|_{H^2}
 \le N^C\|p_N(r\,\cdot)\|_{H^2}.                           \tag{3}
\]
At radius one all four norms have the sharp logarithmic rate
\[
 \log\|V_N\|_{H^2},\ \log\|U_N\|_{H^2},\
 \log\|v_N\|_{H^2},\ \log\|u_N\|_{H^2}
       =\frac{Nv_3}{2\pi}+O(\log N),                       \tag{4}
\]
where \(v_3\) is the regular ideal-tetrahedron volume used in P.
The assertion in (4) is about radius one; (3) also permits radii
depending arbitrarily on \(N\).

## 2. Square integrability at every root

Put \(\zeta_j=Q^{-j}\), \(\beta_j=(N-1-2j)/(2N)\).
P's exact factorization is
\[
 V_N(z)=\prod_{j=0}^{N-1}(1-Q^jz)^{\beta_j},\qquad
                  -\tfrac12<\beta_j<\tfrac12.              \tag{5}
\]
For each fixed \(N\), near \(\zeta_j\) the other factors form a
holomorphic unit. The two boundary square moduli therefore have local
powers \(2\beta_j\) and \(-2\beta_j\), both greater than \(-1\).
They are integrable. The same powers dominate radial approaches:
for \(r\ge1/2\), \(|1-re^{i\varphi}|\ge c|\varphi|\) near zero,
while positive powers stay bounded. With the other factors bounded
away from their roots, this gives an integrable dominating function
for each fixed \(N\). Away from the roots the radial limits are uniform.
Dominated convergence and Parseval for \(r<1\) prove that both
functions belong to \(H^2\), and their norms equal their boundary
\(L^2\) norms. No bound uniform in \(N\) is claimed in this preliminary
argument; the next step supplies it.

P gives on the unit circle, off the roots,
\[
 |V_N(t)|^2\le N^C e^{Nv_3/\pi}
 \begin{cases}(N|t-\zeta_j|)^{2\beta_j},&|t-\zeta_j|<1/N,\\
 1,&\operatorname{dist}(t,\mu_N)\ge1/N,
 \end{cases}                                               \tag{6}
\]
where \(\mu_N=\{\zeta_j\}\). The estimate for \(U_N\) has
\(-2\beta_j\) in place of \(2\beta_j\).
The root arcs are disjoint. On such an arc, put
\(s=|t-\zeta_j|=2|\sin(\varphi/2)|\).
Since \(s<1/N\le1/2\), its angular measure is bounded by a
universal constant times \(ds\) on each side. For either sign,
\[
 \frac1{2\pi}\int_{|t-\zeta_j|<1/N}
          (N|t-\zeta_j|)^{\pm2\beta_j}\,d\theta
       \le\frac{C}{N(1\pm2\beta_j)}.
\]
The sums of these bounds are at most \(C\log(2N)\), since
\[
 N(1-2\beta_j)=2j+1,\qquad
 N(1+2\beta_j)=2N-1-2j.
\]
Integrating (6) on all arcs and their complement therefore proves
\[
 \|V_N\|_{H^2}^2,\ \|U_N\|_{H^2}^2
                          \le N^C e^{Nv_3/\pi}.             \tag{7}
\]
This includes the nearly nonintegrable endpoint exponents, all
parities, and the removable root when \(\beta_j=0\).

## 3. The original coefficients retain the exponential norm

Both physical heads in (2) have the identical energy
\[
 E_N=\|u_N\|_{H^2}^2=\|v_N\|_{H^2}^2
                         =\sum_{a=0}^d|F_a|^{-2}.           \tag{8}
\]
P proves, uniformly for \(0\le a<N\),
\(\log|F_a|=NJ(a/N)+O(\log N)\), where
\(J(s)=\int_0^s\log(2\sin\pi u)du\).
Also \(J(1/6)=-v_3/(2\pi)\).
Choose \(a\) nearest to \(N/6\). For sufficiently large \(N\),
\(J\) has bounded derivative on the intervening fixed interval, so
\(N|J(a/N)-J(1/6)|\le C\). One actual summand in (8) gives
\[
 E_N\ge N^{-C}e^{Nv_3/\pi}.                                \tag{9}
\]
Increasing \(C\) includes the finitely many smaller levels.
Orthogonal projection gives \(E_N\le\|A_N\|_{H^2}^2\).
Together with (7),(9) this proves (4) and (3) at radius one.
Only coefficient magnitudes enter this norm comparison; the
phase-bearing coefficients themselves remain exactly (2).

## 4. Uniform comparison on every smaller disk

Fix either pair and write \(A_N=\sum a_mz^m\). Put
\[
 E_r=\sum_{m<N}|a_m|^2r^{2m},\qquad
 T_r=\sum_{m\ge N}|a_m|^2r^{2m}.
\]
For \(0<r\le1\), termwise comparison gives
\[
 T_r\le r^{2N}T_1,\qquad
 E_r\ge r^{2(N-1)}E_1,\qquad
 \frac{E_r+T_r}{E_r}\le1+r^2\frac{T_1}{E_1}
                         \le\frac{E_1+T_1}{E_1}.            \tag{10}
\]
The last ratio is bounded by a power of \(N\), by Section 3.
Taking square roots proves (3). At \(r=0\), both functions and
both heads equal one, so the assertion is exact. No limiting
assumption on the radius is needed.

The same comparison retains the actual positive-factorial scalar.
Since \(F_d=N\), finite factorial reversal gives
\[
 \mathcal F_N(z)=Nz^dV_N(Q/z),\qquad
 f_N(z)=\sum_{a=0}^dF_az^a=Nz^dv_N(Q/z).                    \tag{11}
\]
Indeed \(NQ^{d-a}[z^{d-a}]v_N=F_a\); this follows by replacing
\(h\) with \(N-h\) in \(F_d/F_{d-a}\).
For every \(R\ge1\), reflection of Fourier modes multiplies both
norms by the same factor \(NR^d\) and changes the inner radius to
\(1/R\). Thus (3) gives
\[
 \|f_N(R\,\cdot)\|_{L^2(\mathbb T)}
 \le\|\mathcal F_N(R\,\cdot)\|_{L^2(\mathbb T)}
 \le N^C\|f_N(R\,\cdot)\|_{L^2(\mathbb T)}.                 \tag{12}
\]
Its finite part is the orthogonal projection to modes \(0,\ldots,d\).
The original factor \(N\) and reflected monomial have not been removed.

## 5. Source meaning and scope

H already identifies (2) as the physical jets and proves the exact
ordered support identities for the completed cyclic/Hardy network.
C retains the full original source, reflected factorials, Gaussian
weights, caps, Cartan factors and external scalar. This note changes
none of those operators or projectors. The new conclusion is the
polynomial norm comparison with the full scalar symbols, including
all radii and the reflected normalization in (11).

These are estimates for the two symbol vectors and their dilates.
They do not assert a bounded multiplication operator on arbitrary
Hardy inputs, a lower bound for a coherent word contraction, or
nonvanishing of its last marked observation. Norm comparison does
not select a geometric cycle or prove the finite-exception theorem.

## Complete inputs and coverage

| Key | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| P | [Uniform cyclic-root estimate](research_cyclic_atom_near_unit_circle.md) | 258 | a7de0218d347cea79b90e46bb11b6c1c0fd594d43b385f0d40a8bd6a4b9e511e |
| C | [Actual continuous source](actual_continuous_gaussian_cyclic_network.md) | 378 | ee47ebbb53258d84ded684e22b1bdfaf193b7fa9a3c852889bf86cb99eb6930c |
| H | [Cyclic/Hardy source coverage](actual_cyclic_hardy_dilog_network.md) | 399 | bdde89f19901f1df29eeee174c163312bbb40b905852083bd75f0d138e5c65c5 |

P and C are complete proof inputs; H is complete coverage. The
coefficient and Hardy estimates above have direct written proofs.
Only written mathematics and text/hash operations were used.
Earlier finals, public manuscripts and the ledger remain unchanged.
