# The two-ended microscopic kernel with its original normal channels

Private written proof, 23 November 2026.

The original Newton kernel has an entire limit when both colors lie
at distance of order \(N^{-2}\) from \(2\). Both ends of its finite
Newton sum survive. The low end gives the Wilson polynomial at a
fixed physical index; the complementary end vanishes at that value
but contributes to its true first normal. The error is \(O(N^{-1})\),
with every fixed holomorphic parameter derivative.

This concerns the canonical ordinary kernel, without replacing it by
a moderate representative. It supplies neither an orthogonality
transform with the original cap nor an estimate of a closed knot source.

## 1. The original kernel and the limiting series

Let \(N\ge2\), \(d=N-1\), \(\theta=\pi/N\), and set
\[
 s_m=2\sin(m\theta),\quad S_k=\prod_{m=1}^k s_m,\quad S_0=1,
 \qquad c_j=2\cos((2j+1)\theta),
\]
\[
 e_k(Z)=S_k^{-2}\prod_{j<k}(c_j-Z),\qquad
 K_N(Z,W)=\sum_{k=0}^{d}e_k(Z)e_k(W),\qquad
 P_N(Z)=2T_N(Z/2)+2=\prod_{j=0}^{d}(Z-c_j).
 \tag{1}
\]
The repeated roots in \(P_N\) retain the original first normals.
At odd levels the additional root \(-2\) is simple. Define
\[
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 E_{k,N}(\alpha)=(-1)^k e_k(w_N(\alpha)),
\]
\[
 \mathsf E_k(\alpha)=
 \frac{(\tfrac12+i\alpha/(2\pi))_k
       (\tfrac12-i\alpha/(2\pi))_k}{(k!)^2},\qquad
 \mathsf H_m(\alpha)=
 \frac{\cosh^2(\alpha/2)}{\pi^2m^2\mathsf E_m(\alpha)}
 \quad(m\ge1).
 \tag{2}
\]
Here \(\mathsf E_0=1\). Every \(\mathsf H_m\) means its entire
continuation: the zeros of \(\mathsf E_m\) are the simple zeros
\(\alpha=\pm i(2r+1)\pi\), \(0\le r<m\), whereas the numerator
has a double zero at each of them. Both families are even.

**Theorem.** The series
\[
 \boxed{\quad
 \mathcal K(\alpha,\beta)=
 \sum_{k=0}^{\infty}\mathsf E_k(\alpha)\mathsf E_k(\beta)
 +\sum_{m=1}^{\infty}\mathsf H_m(\alpha)\mathsf H_m(\beta)
 \quad}
 \tag{3}
\]
converge normally on every compact complex bidisk. They define an
entire symmetric function, even in each variable. For every fixed
\(A<\infty\) and nonnegative integers \(a,b\),
\[
 \sup_{|\alpha|,|\beta|\le A}
 \left|\partial_\alpha^a\partial_\beta^b
  \{K_N(w_N(\alpha),w_N(\beta))-\mathcal K(\alpha,\beta)\}\right|
 \le \frac{C_{A,a,b}}{N}.
 \tag{4}
\]
The estimate holds for all sufficiently large \(N\), through both
parities. For real parameters (3) is a positive Gram kernel; this
does not change the original bilinear closing functional.

## 2. Exact complementary coefficients and uniform tails

The sine product and the full physical polynomial give exactly
\[
 S_{N-1}=N,\qquad P_N(w_N(\alpha))=4\cosh^2(\alpha/2),
\]
\[
 E_{N-m,N}(\alpha)=
 \frac{4\cosh^2(\alpha/2)}{N^2s_m^2E_{m,N}(\alpha)}
 \qquad(1\le m<N).
 \tag{5}
\]
Indeed the last \(m\) roots of \(P_N\) are the first \(m\) roots
in reverse order, and \(S_{N-m}=N/S_{m-1}\). Cancellation in
the full product proves (5); at zeros it is the removable identity.

We recall, and justify, the uniform bound
\[
 |E_{i,N}(\alpha)|\le \frac{C_A}{\min(i,N-i)}
 \qquad(1\le i<N,\ |\alpha|\le A).
 \tag{6}
\]
At zero parameter, for \(i\le N/2\),
\[
 E_{i,N}(0)=\prod_{r<i}
 \left\{\frac{\sin((r+\tfrac12)\theta)}
                  {\sin((r+1)\theta)}\right\}^{\!2}
 \asymp\left\{\frac{(1/2)_i}{i!}\right\}^{\!2}
 \asymp\frac1{i+1}.
 \tag{7}
\]
The first comparison has absolute constants: for
\(f(v)=\sin v/v\), the product of its half-step ratios lies
between \(1\) and \(1/f(i\theta)\le\pi/2\). The second is
the elementary central-binomial, or Wallis, bound. Formula (5),
\(s_m\ge4m/N\) for \(m\le N/2\), and the lower bound in (7)
give the other half of (6) at \(\alpha=0\).

For complex \(|\alpha|\le A\),
\[
 |w_N(\alpha)-2|\le2\cosh(A/N)-2,
\]
\[
 \frac{|e_i(w_N(\alpha))|}{|e_i(2)|}
 \le\prod_{r<i}\left(1+
       \frac{2\cosh(A/N)-2}{2-c_r}\right)
 \le\frac{P_N(w_N(A))}{P_N(2)}=\cosh^2(A/2).
 \tag{8}
\]
All \(2-c_r\) are positive. This proves (6), without discarding
the repeated roots or either end of the Newton list.

## 3. A sharper unit comparison on a linear range

Write \(\operatorname{sinc}z=\sin z/z\) and
\(\operatorname{sinhc}z=\sinh z/z\), with removable values one.
The exact difference of cosines gives
\[
 E_{i,N}(\alpha)=\mathsf E_i(\alpha)U_{i,N}(\alpha),
\]
\[
 U_{i,N}(\alpha)=\prod_{r=0}^{i-1}
 \frac{\operatorname{sinhc}((\alpha+i(2r+1)\pi)/(2N))
       \operatorname{sinhc}((\alpha-i(2r+1)\pi)/(2N))}
      {\operatorname{sinc}(\pi(r+1)/N)^2}.
 \tag{9}
\]
This factorization is valid at zeros of \(\mathsf E_i\).
For \(i\le N/4\), all displayed factors are units on a fixed
bounded \(\alpha\)-disk once \(N\) is sufficiently large.
We claim
\[
 |U_{i,N}^{\ \pm1}-1|\le C_A\frac{i^2}{N^2}
 \qquad(1\le i\le N/4,\ |\alpha|\le A).
 \tag{10}
\]

Here is the cancellation that gives the linear-range estimate.
Put \(v_r=(r+1/2)\pi/N\), \(h=\pi/(2N)\), and
\(a=\alpha/(2N)\). At \(\alpha=0\), a continuous logarithm gives
\[
 \log U_{i,N}(0)=2\sum_{r<i}
       \{\log\operatorname{sinc}v_r
                    -\log\operatorname{sinc}(v_r+h)\}
                =O(i^2/N^2).
 \tag{11}
\]
Indeed \((\log\operatorname{sinc})'(v)=O(v)\) on a fixed
neighborhood of \([0,\pi/4]\). Let
\(g(z)=\log\operatorname{sinhc}z\), with \(g(0)=0\), on a
fixed zero-free disk containing all \(a\pm iv_r\). It is even.
The function
\(g(a+iv_r)+g(a-iv_r)-2g(iv_r)\) is even in \(a\), vanishes
at zero, and is \(O_A(N^{-2})\) by its uniformly bounded second
derivative. Summing over \(r<i\) and using (11) gives
\(|\log U_{i,N}(\alpha)|\le C_Ai^2/N^2\).
This logarithm is bounded on the entire stated range; exponentiating
both signs proves (10). It need not tend to zero at \(i=N/4\).

Combining (5) and (9) gives the entire identity
\[
 E_{N-m,N}(\alpha)=\mathsf H_m(\alpha)
       \operatorname{sinc}(\pi m/N)^{-2}U_{m,N}(\alpha)^{-1}.
 \tag{12}
\]
It follows first off the zeros and then at them by continuation.
For each fixed index, (9) and (12) give respectively the limits
\(\mathsf E_i\) and \(\mathsf H_m\), uniformly on compact disks.
Passing (6) to these limits proves
\[
 \sup_{|\alpha|\le A}
       (|\mathsf E_m(\alpha)|+|\mathsf H_m(\alpha)|)
                         \le C_A/m\qquad(m\ge1).
 \tag{13}
\]
In particular both series in (3) converge normally, including all
their apparently singular parameter values.

## 4. Summing the two ends and retaining derivatives

Let \(L=\lfloor N/4\rfloor\). Split the canonical finite sum into
\(0\le i\le L\), \(i=N-m\) with \(1\le m\le L\), and the
remaining middle. There is no overlap for large \(N\).
Since the two signs \((-1)^i\) cancel in every same-index product,
these are products of the \(E_{i,N}\) defined above.

For \(1\le i\le L\), (9)--(10) and (13) give
\[
 |E_{i,N}(\alpha)E_{i,N}(\beta)
       -\mathsf E_i(\alpha)\mathsf E_i(\beta)|
 \le \frac{C_A}{i^2}\frac{i^2}{N^2}=\frac{C_A}{N^2}.
 \tag{14}
\]
The index-zero terms agree exactly. The high products obey the same
bound by (12), since
\(\operatorname{sinc}(\pi m/N)^{-2}-1=O(m^2/N^2)\).
Summing these errors costs \(O_A(N^{-1})\). By (6), the middle
sum is bounded by
\(C_A\sum_{L<i<N-L}\min(i,N-i)^{-2}=O_A(N^{-1})\).
Both infinite tails after \(L\) are \(O_A(N^{-1})\) by (13).
This proves (4) for \(a=b=0\). Prove it on a larger bidisk and
apply Cauchy's formula to obtain every stated mixed derivative,
with the same rate. The Gram assertion follows directly from (3),
whose two coefficient families are real at real parameters.

## 5. The fixed-index value and its true first normal

Put
\[
 \mathscr K(r,\alpha)=\mathcal K(\alpha,i\pi(2r+1)).
\]
For every fixed integer \(j\ge0\),
\[
 \mathscr K(j,\alpha)=
 {}_4F_3\!\left(\begin{matrix}-j,j+1,
       \tfrac12+i\alpha/(2\pi),\tfrac12-i\alpha/(2\pi)\\
                         1,1,1\end{matrix};1\right).
 \tag{15}
\]
In fact \(\mathsf E_k(i\pi(2j+1))=0\) for \(k>j\), while
every \(\mathsf H_m(i\pi(2j+1))=0\). This is the normalized
Wilson value \(W_j((\alpha/(2\pi))^2;1/2,1/2,1/2,1/2)/(j!)^3\).

The complementary series cannot be discarded before differentiation.
Termwise differentiation is allowed by normal convergence, and
\[
 \left.\partial_r\mathsf H_m(i\pi(2r+1))\right|_{r=j}
 =\begin{cases}
 0,&m\le j,\\
 \displaystyle(-1)^{j+1}
       \frac{((m-1)!)^2}{(m-j-1)!(m+j)!},&m>j.
 \end{cases}
 \tag{16}
\]
To check this, substitute
\(\mathsf E_m(i\pi(2r+1))=(-r)_m(r+1)_m/(m!)^2\)
and \(\cosh^2(i\pi(2r+1)/2)=\sin^2\pi r\) in (2).
For \(m>j\), the factor \(\mathsf E_m(i\pi(2r+1))\) has one
simple zero, of derivative
\((-1)^{j+1}(m-j-1)!(m+j)!/(m!)^2\); for \(m\le j\) it is nonzero.

Writing \(c_N(r)=2\cos((2r+1)\pi/N)\), (4) and the chain rule give
\[
 \boxed{\quad
 \frac{\partial_Z K_N(c_j,w_N(\alpha))}{N^2}
 =-\frac{\partial_r\mathscr K(j,\alpha)}{4\pi^2(2j+1)}
                                      +O_{A,j}(N^{-1}).
 \quad}
 \tag{17}
\]
Indeed \(N^2c_N'(j)=-4\pi^2(2j+1)+O_j(N^{-2})\).
Every fixed \(\alpha\)-derivative retains the estimate.
For fixed \(j\), this is its original double-root normal at all
sufficiently large levels; no normal at the moving odd simple node
has been introduced.

At \(j=0\), differentiation of the low series gives
\(-\sum_{m\ge1}\mathsf E_m(\alpha)/m\); (16) gives
\(-\sum_{m\ge1}\mathsf H_m(\alpha)/m\) for the high series.
Consequently the earlier endpoint function is
\[
 \mathcal Q(\alpha)=\frac1{4\pi^2}
       \sum_{m\ge1}\frac{\mathsf E_m(\alpha)+\mathsf H_m(\alpha)}m,
 \qquad
 N^{-2}\partial_ZK_N(c_0,w_N(\alpha))
                       =\mathcal Q(\alpha)+O_A(N^{-1}).
 \tag{18}
\]
Thus its previous \(O(N^{-1/2})\) rate improves to \(O(N^{-1})\),
including every fixed parameter derivative. Both series in (18)
are positive for real \(\alpha\).

## 6. Source scope and complete coverage

For the original ordinary Askey--Wilson operator, write
\[
 (\mathcal L f)(c_N(r))=(c_0+A_N(r)+C_N(r))f(c_N(r))
       -A_N(r)f(c_N(r+1))-C_N(r)f(c_N(r-1)),
\]
where \(A_N(r)=s_{r+1}^4/(s_{2r+1}s_{2r+2})\),
\(C_N(r)=s_r^4/(s_{2r}s_{2r+1})\), and
\(s_r=2\sin(\pi r/N)\). Combined expressions are continued through
their apparent poles. The exact full kernel obeys
\[
 wK_N(z,w)-\mathcal L_zK_N(z,w)
                 =\frac{(-1)^{N-1}}{N^2}P_N(w)e_{N-1}(z).
 \tag{19}
\]
The endpoint first normal of its right side, at \(z=c_0\) and
\(w=w_N(\alpha)\), is
\(4\cosh^2(\alpha/2)/(N^2s_1^2)\to\cosh^2(\alpha/2)/\pi^2\).
This source is retained. We have not identified (3) with a standard
homogeneous Wilson function or imported a Wilson orthogonality theorem.
The Wilson name in (15) uses only its defining terminating formula.

The estimates concern bounded microscopic parameters and fixed physical
indices. They are not uniform over all \(j\) of order \(N\), arbitrary
outer turns, or original cap contractions after a general short word.
Neither Gram positivity nor the nonzero endpoint normal changes the
original closing into an adjoint norm or proves a geometric coefficient.

The earlier two-ended result treated one endpoint normal; its uniform
coefficient bound and exact unit factorization are retained here.
The connection note treated values and their growing bulk overlap.
The shared-current note explicitly retained doubly microscopic edges
as additional joint amplitudes. None supplies the full limit (3)--(4).
The complete texts below were read at matching versions before writing:

| Role | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| Input | [Two-ended endpoint normal](research_endpoint_normal_two_ended_limit.md) | 379 | 1e72bffbd0718fec2ae61c7a91dbb93bcd1506a8ca3db28f030cc8fcb2400e93 |
| Input | [Full kernel source](research_edge_kernel_difference_and_endpoint_bound.md) | 399 | 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da |
| Coverage | [Endpoint value connection](research_endpoint_value_connection_and_overlap.md) | 682 | 87801bd8baca255a86fdbcd5170662fd9f2b366f983507f776d5676fd8a324da |
| Coverage | [Shared microscopic current](research_shared_microscopic_current_mode_integration.md) | 405 | 8b1de1424b19f00cea165bff93fd71892e218749247b733c9abbdc9797ae67fb |

The [DLMF Wilson definition](https://dlmf.nist.gov/18.26.E1) was checked
for terminology only. No external asymptotic or orthogonality proof is
used. Only written mathematics and text/hash operations were performed;
no mathematical program, numerical experiment, test, build, git operation
or previously finalized file edit was made.
