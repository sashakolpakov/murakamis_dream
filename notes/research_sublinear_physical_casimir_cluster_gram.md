# Sublinear clusters of the actual physical Casimir frame

Written proof, 24 November 2026.

Any sublinear number of distinct physical Casimir blocks has a
subexponentially conditioned joint frame after each individual block
is Hermitian orthonormalized. The selected blocks may be anywhere in
the spectrum and need not be consecutive. Every actual first normal
in a double block is retained. The estimate holds at every physical
pair degree, including its recorded high-degree mirror.

The interpolation estimate behind the proof is already present in
[S]. The source conclusion here is a bound for arbitrary coefficients
in a growing sum of actual physical invariant spaces. It is stronger
than an entrywise overlap estimate. It is not an ambient spectral
projection bound, and raw column norms and inverse measures remain.

For near-fold blocks on a strict real degree compact, the positive
energy estimate in [F] supplies a further conclusion. The whole
orthonormalized cluster is exponentially isotropic for the original
bilinear pairing, while its conjugate adjoint-Casimir cluster gives
an asymptotically orthonormal doubled frame and a bilinear block swap.
No arbitrary original exterior is asserted to produce that adjoint
carrier or a nonzero marked closing.

## 1. The original blocks and their exact normalization

Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
First take an original physical pair degree \(0\le t\le d\),
with physical basis \(|u,t-u\rangle\), \(0\le u\le t\),
orthonormal. The actual Casimir matrix \(J_t\) is complex symmetric.
Its entries, with \(U_u=Q^u\), \(T=Q^t\), are
\[
 \begin{split}
 D_u&=\frac{U_u}{T}
       [2(q^{-1}+qT)-(q+q^{-1})U_u],\\
 A_u&=(U_u-T)(1-QU_u)/T\quad(0\le u<t).
 \end{split}
 \tag{1}
\]
Thus \(|D_u|\le6\), \(|A_u|\le4\), and the row and column
sum bounds give
\[
                         \|J_t\|\le14 .
 \tag{2}
\]
All norms below are physical Euclidean or induced operator norms.
For a high physical degree \(d<t'\le2d\), [H] identifies its
root matrix with \(J_{2d-t'}\) by the recorded unitary index
translation. Apply the following constructions through that map.
This is a root-level transport of the actual columns; no new flat
generic-\(q\) duality is assumed.

The characteristic polynomial is the original
\[
 P_t(Z)=\prod_{r=0}^t(Z-c_r),\qquad
 c_r=q^{2r+1}+q^{-2r-1}.
 \tag{3}
\]
Every distinct node has multiplicity one or two. A double is exactly
\(j,l=d-j\) with \(j<l\le t\); the odd self-paired node is simple.
At a simple node use its original normalized column \(C_i\).
At a double node use the actual value and normal \((C_i,w_i)\).
They satisfy
\[
 (J_t-c_i)C_i=0,\qquad (J_t-c_i)w_i=C_i .
 \tag{4}
\]
The normal in (4) is the generic divided derivative with divisor
\(-2N(q^{2j+1}-q^{-2j-1})\), as in [H,G]. It is not an
independently chosen generalized eigenvector. The first component
of \(C_i\) is one.

For a double define
\[
 \alpha_i=\frac{\langle C_i,w_i\rangle}{\|C_i\|^2},\quad
 d_i=\frac{\|w_i-\alpha_iC_i\|}{\|C_i\|},\quad
 E_i=\left(\frac{C_i}{\|C_i\|},
          \frac{w_i-\alpha_iC_i}{\|C_i\|d_i}\right).
 \tag{5}
\]
The two columns are exactly Hermitian orthonormal. They are independent
by (4), so \(d_i>0\). For a simple block set \(E_i=C_i/\|C_i\|\).
Write \(\nu_i=1\) or \(2\) for its actual block dimension.
At a double the exact restriction is
\[
 J_tE_i=E_i
          \begin{pmatrix}c_i&d_i^{-1}\\0&c_i\end{pmatrix}.
 \tag{6}
\]

The source adapter in each double block has polynomial cost at every
physical degree. Indeed (2),(4) give
\(\|C_i\|\le16\|w_i-\alpha_iC_i\|\), while [G] gives
\(\|w_i\|\le C N^6\|C_i\|\). Consequently
\[
 \frac1{16}\le d_i\le C N^6,\qquad |\alpha_i|\le C N^6.
 \tag{7}
\]
In particular, for the actual canonical columns normalized by their
common value-column norm,
\[
 F_i:=\left(\frac{C_i}{\|C_i\|},\frac{w_i}{\|C_i\|}\right)
       =E_iS_i,\qquad
 S_i=\begin{pmatrix}1&\alpha_i\\0&d_i\end{pmatrix},\qquad
 \|S_i\|+\|S_i^{-1}\|\le C N^6 .
 \tag{8}
\]
For a simple block take \(F_i=E_i\) and \(S_i=1\).
No bound removes the possibly exponential, explicitly known
per-block scalar \(\|C_i\|\) from the raw source columns.

## 2. The whole selected-cluster estimate

Select any \(m\ge1\) distinct nodes occurring in this one physical
block, with every column of each selected simple or double block.
The nodes need not form a consecutive window. Put
\[
 r=\sum_{i=1}^m\nu_i,\qquad
 V=(E_1,\ldots,E_m),\qquad
 {\cal L}_{N,m}=m\log(eN/m)+\log N .
 \tag{9}
\]
Here \(m\le N\), so the logarithm is positive.

**Theorem 1.** There is an absolute constant \(C\) such that,
at every physical degree and for every selected set,
\[
 \boxed{\qquad
 e^{-C{\cal L}_{N,m}}I_r\ \le\ V^*V\ \le\ mI_r .
 \qquad}
 \tag{10}
\]
The same exponential form, after increasing \(C\), holds for
\(W=(F_1,\ldots,F_m)\) in place of \(V\), with an upper bound
\(CmN^{12}I_r\). Thus both frames have
\[
 \log\operatorname{cond}_2(V^*V),\quad
 \log\operatorname{cond}_2(W^*W)
                         \le C{\cal L}_{N,m}.
 \tag{11}
\]
All coefficients in these inequalities are arbitrary. They are not
restricted to slowly varying or fixed-dimensional channel families.
For any sequence \(m_N=o(N)\), the frame and Gram condition
numbers in (11) are \(\exp(o(N))\), uniformly over the selected
nodes and physical degrees.

### Actual cosine separation and the factorial denominator

Label the distinct nodes by their canonical indices
\(0\le a\le\lfloor d/2\rfloor\), and sort the selected indices
as \(a_1<\cdots<a_m\). For \(a<b\), put \(k=b-a\).
Then \(k\le a+b+1\le N-k\), and \(k\le N/2\), so
\[
 \begin{split}
 |c_a-c_b|
 &=4\sin((a+b+1)\pi/N)\sin(k\pi/N)\\
 &\ge16 k^2/N^2.
 \end{split}
 \tag{12}
\]
In particular \(|c_{a_i}-c_{a_k}|\ge16|i-k|^2/N^2\).
For every selected index \(i\), this gives
\[
 \prod_{k\ne i}|c_i-c_k|
 \ge(16/N^2)^{m-1}\{(i-1)!(m-i)!\}^2.
 \tag{13}
\]
The notation \(c_i\) from now on refers to the selected ordered node.
Since
\((i-1)!(m-i)!\ge(m-1)!/2^{m-1}\), the lower bound keeps
the factorial improvement when \(m\) grows. Replacing every
gap separately by \(N^{-2}\) would lose this improvement.

### Exact Hermite filters on the selected union

Use the full multiplicity of each selected block and define
\[
 q_i(Z)=\prod_{k\ne i}(Z-c_k)^{\nu_k},\qquad
 \ell_i(Z)=q_i(Z)/q_i(c_i),
\]
\[
 h_i(Z)=
 \begin{cases}
  \ell_i(Z),&\nu_i=1,\\
  [1-\ell_i'(c_i)(Z-c_i)]\ell_i(Z),&\nu_i=2.
 \end{cases}
 \tag{14}
\]
These are the selected value-cardinals of the Hermite interpolation
bound in [S]. Their value at \(c_i\) is one, and their first
derivative there is zero when that normal exists. At any other
selected node they vanish to its full multiplicity. Therefore
\[
                         h_i(J_t)E_k=\delta_{ik}E_k .
 \tag{15}
\]
The derivative-zero condition in (14) retains the Jordan column;
it does not replace a double block by its value line.

For completeness, the quantitative interpolation argument is repeated
here with the operator evaluated directly at the actual \(J_t\).
Every gap is at most four. Since \(\nu_k\in\{1,2\}\),
\[
 |q_i(c_i)|\ge4^{-(m-1)}
                 \left(\prod_{k\ne i}|c_i-c_k|\right)^2 .
 \tag{16}
\]
Also \(\|J_t-c_k I\|\le16\), and (12) gives
\[
 |\ell_i'(c_i)|
  =\left|\sum_{k\ne i}\frac{\nu_k}{c_i-c_k}\right|
  \le C N^2\sum_{k\ne i}|i-k|^{-2}\le C'N^2.
 \tag{17}
\]
For \(m\ge2\), equations (13),(16) and
\((m-1)!\ge((m-1)/e)^{m-1}\) consequently prove
\[
 L_{N,m}:=\max_i\|h_i(J_t)\|
       \le\exp\{C[m\log(eN/m)+\log N]\}.
 \tag{18}
\]
Indeed the numerator of \(q_i(J_t)\) costs at most
\(16^{2(m-1)}\), the reciprocal denominator costs at most
\((CN)^{4(m-1)}/((m-1)!)^4\), and (17) adds only a
fixed power of \(N\). For \(m=1\), the filter is exactly one,
so (18) holds as well. The proof of [S, Lemma 2] uses the same
factorial mechanism for consecutive row windows. Inequality (12)
shows directly why arbitrary selected indices have the same bound.
No new general interpolation method is claimed.

### Recovery on the actual selected invariant sum

For arbitrary coefficient packets \(a_i\in\mathbb C^{\nu_i}\),
put \(v=\sum_iE_i a_i\). By (15) and block orthonormality,
\[
                  \|a_i\|=\|h_i(J_t)v\|
                              \le L_{N,m}\|v\|.
 \tag{19}
\]
Summing their squares gives
\(\|v\|^2\ge(mL_{N,m}^2)^{-1}\sum_i\|a_i\|^2\).
Conversely the triangle and Cauchy--Schwarz inequalities give
\(\|v\|^2\le m\sum_i\|a_i\|^2\).
Together with (18), these prove (10). Formula (8), applied to the
block diagonal adapter, proves (11) for the source columns too.
Finally, if \(m=o(N)\),
\[
 \frac{{\cal L}_{N,m}}N
    =\frac mN\log\frac{eN}{m}+\frac{\log N}N\longrightarrow0,
 \tag{20}
\]
which proves the asserted uniform subexponential cost.

The uniform degree estimate also gives a full pair-boundary version.
Physical total-degree blocks are mutually Hermitian orthogonal, so
the direct sum of selected frames over all degrees has a direct-sum
Gram. Its logarithmic conditioning costs at most
\(C\max_t{\cal L}_{N,m_t}\), with no factor for the number of
degrees; empty blocks are omitted. For a fixed number \(k\) of
disjoint physical pairs, take the tensor product of these boundary
frames. Its Gram is the tensor product of their Grams, so
\[
 \log\operatorname{cond}_2\operatorname{Gram}(V_{\partial})
       \le C\sum_{a=1}^k\max_t{\cal L}_{N,m_{a,t}}.
 \tag{20a}
\]
This is \(o(N)\) if, for each pair, \(\sup_t m_{a,t}=o(N)\).
It controls arbitrary coherent coefficient tensors, not only
separable inputs. Disjoint pairings are essential to this tensor
statement: changing to an overlapping pairing still requires the
actual recoupling map and its source estimate.

The filters (14) are **not** the ambient spectral projectors.
Their action on unselected blocks is not zero in general. Equation
(19) applies to the selected invariant sum, not to an arbitrary
original vector before its unselected part is controlled. At \(m=1\)
the filter is the identity, even when the actual ambient projector
onto that one block has exponential norm. This distinction prevents
an inference about the cost of selecting a physical source sector.

## 3. A doubled adapter for a growing near-fold cluster

Now fix a real compact \(I\Subset(1/2,1)\), take
\(\tau=t/N\in I\), and select only double blocks with
\(s_i=l_i-j_i\le\delta_I N\), where \(\delta_I>0\) is small
enough for [F]. The number \(m\) can grow. Use exactly (5), so
the per-node frames agree with the actual centered physical frames
of [F], not just with arbitrary bases of the same spaces.

At each node [H,F] give the exact bilinear Gram
\[
 B_i:=E_i^{\mathsf T}E_i
 =\frac{\sigma_i}{\|C_i\|^2d_i}
   \begin{pmatrix}0&1\\1&(\eta_i-2\alpha_i)/d_i\end{pmatrix},
 \tag{21}
\]
with the original complex measure and shear retained. The positive
native-energy exponent in [F] implies, uniformly in these blocks,
\[
                           \|B_i\|\le C_I e^{-a_I N}
 \tag{22}
\]
for some \(a_I>0\). This is precisely where the near-fold and
strict-degree hypotheses enter; they were not needed for Theorem 1.
Only the positive native-energy bound from [F] is required here:
\(\|C_i\|^2/|\sigma_i|\ge e^{aN}/\operatorname{poly}(N)\),
together with (7) and \(|\eta_i|\le CN^3\), already proves
(22). Its sharper Gaussian variance is not logically needed for
this cluster consequence.

Distinct actual generalized eigenspaces are orthogonal for the
bilinear transpose pairing because \(J_t^{\mathsf T}=J_t\).
For example apply the same filter (15) on its two sides. Hence
\[
 E_i^{\mathsf T}E_k=0\quad(i\ne k),\qquad
                  V^{\mathsf T}V=\operatorname{diag}(B_i).
 \tag{23}
\]
Let \(A=V^*V\) and orthonormalize the **whole** selected cluster:
\[
                        U=VA^{-1/2},\qquad U^*U=I_{2m}.
 \tag{24}
\]
Theorem 1 and (22),(23) show
\[
 \|U^{\mathsf T}U\|
 \le C_I\exp\{-a_I N+C_I{\cal L}_{N,m}\}.
 \tag{25}
\]
Indeed transpose has the same operator norm, and the two factors
of \(A^{-1/2}\) cost \(\lambda_{\min}(A)^{-1}\).
For every \(m_N=o(N)\), the right side is
\(\exp(-a_I N+o(N))\). This is an operator estimate for the
whole growing cluster, not an entrywise approximation to its Gram.

Retain its actual conjugate carrier and put
\({\cal D}=(U,\overline U)\), \(B=U^{\mathsf T}U\).
The exact doubled identities are
\[
 {\cal D}^*{\cal D}=
       \begin{pmatrix}I&\overline B\\B&I\end{pmatrix},\qquad
 {\cal D}^{\mathsf T}{\cal D}=
       \begin{pmatrix}B&I\\I&\overline B\end{pmatrix}.
 \tag{26}
\]
For sublinear \(m\), their errors from \(I_{4m}\) and the
block swap are \(\exp(-a_I N+o(N))\) in operator norm.
Their singular values therefore lie between \(1-\varepsilon_N\)
and \(1+\varepsilon_N\), with \(\varepsilon_N\to0\)
exponentially. The doubled frame and its bilinear pairing have
condition numbers tending to one.

The selected range of \(U\) is \(J_t\)-invariant. Since the
physical matrix is complex symmetric, \(J_t^*=\overline{J_t}\),
so the range of \(\overline U\) is invariant under the adjoint
Casimir. Whole-cluster orthonormalization can mix the selected
nodes; no individual column of \(U\) is newly declared an eigenvector.
The conjugates are an adjoint carrier, not extra eigenchannels of
the original Casimir. Formula (26) applies only when those two
stated boundary types are actually paired.

## 4. Source meaning and remaining gluing problem

Theorem 1 controls arbitrary coherent coefficient vectors in any
selected sublinear cluster. It requires neither a local Gaussian
approximation nor separation between its selected nodes beyond
the exact physical cosine spacing. The first-normal directions,
simple endpoints, both level parities and all physical degrees remain.

This does not remove the raw per-block value norms, the inverse
Christoffel--Darboux measures, framing phases, pivots, or the original
marked closing. Those known factors must be transported explicitly
when source coefficients are expressed in this frame. A component
outside the selected invariant sum is not bounded by (19).
Neither the ambient spectral complement nor an arbitrary turn or
short component is asserted to preserve the selected cluster.

Likewise (26) supplies a stable pairing for an actual carrier and
its adjoint conjugate. It does not show that an arbitrary original
exterior supplies that adjoint carrier. The original ordinary cap
can annihilate a selected cluster omitting its distinguished source
channel, as [H] records. The marked row is not replaced by an
ordinary cap or by a Hermitian norm. No lower bound for its projection
onto this growing cluster is inferred.

The closest prior estimate [S] is the same factorial Hermite bound
for analytic spectral repair. The fixed-window result [R] instead
gives polynomial recovery for a fixed number of analytic source rows
on a nonzero-minor chart. It is not the unconditional growing-block
statement (10). The new conclusions here concern their source
application to the actual bounded physical Casimir and, using [F],
the operator-level doubled adapter for a sublinear cluster.
No original knot-volume lower bound or finite-exception theorem is
claimed without the further source, exterior and closing estimates.

## Complete proof inputs and closest coverage

All five complete texts were read at their matching versions.

| Label | Complete text | SHA256 |
| --- | --- | --- |
| H | [Complete actual Hermite packet](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_casimir_hermite_packet.md), 321 lines | a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c |
| G | [Physical-grid actual normal](actual_q_hahn_physical_partner_normal_bound.md), 232 lines | 0725b210bd16899260533cf7a1a7aa9602a7ed0b0e18baf4831efb7a968e07d3 |
| S | [Short physical spectral-window repair](research_short_spectral_window_repair.md), 405 lines | 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550 |
| F | [Full physical Gaussian--Hermite Gram](research_q_hahn_physical_normal_gaussian_gram.md), 476 lines | c28e236e33674ae93644ac255465944ab11b58883d1851637a2319fa6696b2f4 |
| R | [Fixed resonant physical-window conditioning](research_resonant_physical_window_conditioning.md), 267 lines | f1af212ec05ffdb79cc9b99ce03961622740d58622213e648918000e81e5fa07 |

Only written mathematics, complete text reads, and metadata hashes
were used. No mathematical program, numerical experiment, test,
build, earlier-final edit, or public-manuscript change was made.
