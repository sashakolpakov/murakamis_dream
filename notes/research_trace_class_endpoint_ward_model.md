# A trace-class endpoint model for the actual cut Ward current

Written proof, 24 November 2026.

The original binomial cut has a controlled endpoint limit, including
its entire rescaled Ward current and every fixed micro-meridian jet.
The current, both products with the limiting unbounded lowering
operator, and their commutator converge in trace norm at rate
\(O(N^{-1})\). This is a statement about the actual boundary operators
before pairing with an exterior; it is not a large-level estimate
for the exterior or its geometric framing period.

## 1. The original finite source and the endpoint scaling

Use the orthonormal factorial head basis of [I], with
\[
 N\ge2,\quad d=N-1,\quad Q_N=e^{2\pi i/N},\qquad
 M=e^{u/N},\quad \theta=\lambda/N,\quad |u|<\pi .
 \tag{1}
\]
The parameters \(u,\lambda\) are complex. For real \(\lambda\ge0\)
and sufficiently large \(N\), the cut weights below are probabilities;
elsewhere their formulas mean holomorphic coefficients.
The original lowering matrix is
\[
 \mathcal E_N|a\rangle
   =\epsilon_{N,a-1}(u)|a-1\rangle\quad(1\le a<N),\qquad
 \mathcal E_N|0\rangle=0,\qquad
 \epsilon_{N,r}=e^{u/N}Q_N^{-r-1}-e^{-u/N}.
 \tag{2}
\]
No outward endpoint arrow is added.

Embed this basis into \(\mathcal H=\ell^2(\mathbb N_0)\), and extend
finite matrices by zero. Define the coefficients and tails by
\[
 p_{N,a}=\binom{N-1}{a}(\lambda/N)^a(1-\lambda/N)^{N-1-a}
 \quad(0\le a<N),\qquad p_{N,a}=0\quad(a\ge N),
\]
\[
 T_{N,r}=\sum_{a>r}p_{N,a},\qquad
 P_N=\sum_{a\ge0}p_{N,a}|a\rangle\langle a|,\qquad
 P_0=|0\rangle\langle0|.
 \tag{3}
\]
The notation \(P_0\) always means this fixed vacuum projection.
In particular \(T_{N,r}=0\) for \(r\ge N-1\), and
\(\operatorname{Tr}P_N=1\). Put
\[
 D_N=N\mathcal E_N,\qquad
 B_N=-\sum_{r=0}^{N-2}
          \frac{T_{N,r}}{N\epsilon_{N,r}(u)}
                         |r+1\rangle\langle r|.
 \tag{4}
\]
These are precisely [I,S]'s actual cut current and lowering matrix
with opposite scalar rescalings. Every finite denominator is a unit
on \(|u|<\pi\), as also proved below.

Multiplication cancels each denominator exactly:
\[
 \begin{split}
 D_NB_N&=-\operatorname{diag}(T_{N,0},T_{N,1},\ldots),\\
 B_ND_N&=-\operatorname{diag}(0,T_{N,0},T_{N,1},\ldots),\\
 [D_N,B_N]&=P_N-P_0 .
 \end{split}
 \tag{5}
\]
Thus for every actual finite marked cut matrix \(C\),
\[
 \operatorname{Tr}((P_N-P_0)C)
                 =\operatorname{Tr}(B_N[C,D_N]).
 \tag{6}
\]
All original crossings, tail pivots, marks and scalar lines remain in
\(C\). For the original unmarked knot cut, [I] gives
\(C_N(M)=F_N(M)I\), so either trace-one probe computes the same
original scalar. Equation (6), rather than equality of arbitrary
marked probes, is the source-preserving statement used here.
The rescaling in (4) changes neither (5) nor (6).

## 2. The whole limiting operators

Let
\[
 p_a(\lambda)=e^{-\lambda}\lambda^a/a!,\quad
 \tau_r(\lambda)=\sum_{a>r}p_a(\lambda),\quad
 P(\lambda)=\operatorname{diag}(p_0,p_1,\ldots),
\]
\[
 B(u,\lambda)=
   \sum_{r\ge0}\frac{\tau_r(\lambda)}
                       {2(\pi i(r+1)-u)}
                           |r+1\rangle\langle r|.
 \tag{7}
\]
Every tail is entire in \(\lambda\). The series defines a
trace-class operator, holomorphic for \(|u|<\pi\) and entire
in \(\lambda\), in the trace-class norm.

The limiting lowering operator is the closed weighted shift
\[
 D_u|0\rangle=0,\qquad
 D_u|a\rangle=(2u-2\pi ia)|a-1\rangle\quad(a\ge1),
\]
\[
 \operatorname{Dom}D_u=
     \left\{v\in\mathcal H:\sum_{a\ge1}a^2|v_a|^2<\infty\right\}.
 \tag{8}
\]
The displayed domain is independent of \(u\) in the stated disk.
Closedness follows directly by taking coordinates in a convergent
graph sequence. The tail estimates below show that \(B\) maps
\(\mathcal H\) into this domain. They also give
\[
 D_uB=-\operatorname{diag}(\tau_0,\tau_1,\ldots),\qquad
 BD_u=-\operatorname{diag}(0,\tau_0,\tau_1,\ldots).
 \tag{9}
\]
The second identity first holds on \(\operatorname{Dom}D_u\);
its right side is its unique bounded extension to \(\mathcal H\).
Both operators in (9) are trace class. In particular the commutator
below means the difference of these specified trace-class products:
\[
                         [D_u,B]=P(\lambda)-P_0 .
 \tag{10}
\]
There is no claim of operator-norm convergence of the unbounded
generators themselves.

**Theorem.** For every compact
\(K\subset\{(u,\lambda)\in\mathbb C^2:|u|<\pi\}\), uniformly on \(K\),
\[
 \begin{split}
 &\|B_N-B\|_1+\|P_N-P\|_1\\
 &\quad+\|D_NB_N-D_uB\|_1
           +\|B_ND_N-BD_u\|_1\le C_K/N .
 \end{split}
 \tag{11}
\]
The same bound holds after any fixed mixed derivatives in
\(u,\lambda\), with a constant depending on their orders and \(K\).
The symbol \(\|\cdot\|_1\) is trace norm on the stated orthonormal
head space. No comparison with a full knot-period norm is made.

## 3. A weighted coefficient estimate

For \(\lambda\) in a fixed complex compact set, the generating functions
are
\[
 G_N(z,\lambda)=\sum_a p_{N,a}z^a
       =(1+\lambda(z-1)/N)^{N-1},\qquad
 G(z,\lambda)=e^{\lambda(z-1)}.
 \tag{12}
\]
On \(|z|=2\), the Taylor expansion of the logarithm gives
\((N-1)\log(1+\lambda(z-1)/N)=\lambda(z-1)+O_K(N^{-1})\).
The error is uniform for all sufficiently large \(N\). Exponentiation
and the coefficient Cauchy formula therefore give
\[
 |p_{N,a}-p_a|\le C_KN^{-1}2^{-a},\qquad
 |p_{N,a}|+|p_a|\le C_K2^{-a}\quad(a\ge0).
 \tag{13}
\]
The first estimate includes the zero-extended finite coefficients.
Summing coefficients above \(r\) proves
\[
 |T_{N,r}-\tau_r|\le C_KN^{-1}2^{-r},\qquad
 |T_{N,r}|+|\tau_r|\le C_K2^{-r}.
 \tag{14}
\]
In particular all fixed polynomially weighted \(\ell^1\) versions
of these errors are \(O_K(N^{-1})\). These estimates prove the
trace-class assertions for \(P,B\), and also
\(\sup_r(r+1)|B_{r+1,r}|<\infty\), which justifies the domain
claim before (9).

For clarity, a diagonal matrix has trace norm equal to the sum of
the absolute values of its entries. A shift
\(\sum b_r|r+1\rangle\langle r|\) has the same formula for its
trace norm: its adjoint times itself is
\(\operatorname{diag}(|b_r|^2)\). Thus these coefficient estimates
control the entire operators, rather than each fixed index alone.

## 4. The original denominators and the current limit

Write \(k=r+1\). The exact factorization is
\[
 N\epsilon_{N,k-1}(u)
       =2N e^{-\pi ik/N}\sinh((u-\pi ik)/N).
 \tag{15}
\]
Fix \(|u|\le R<\pi\). Since
\(|\sinh(x+iy)|^2=\sinh^2x+\sin^2y\), and
\(|\sin y|\ge(2/\pi)\operatorname{dist}(y,\pi\mathbb Z)\), it follows
for \(1\le k<N\) that
\[
 |N\epsilon_{N,k-1}(u)|
             \ge c_R\min(k,N-k),\qquad
 |2(u-\pi ik)|\ge2(\pi-R)k .
 \tag{16}
\]
Indeed the sine argument lies strictly between \(-\pi\) and zero,
and its distance from either endpoint is at least
\((\pi-R)\min(k,N-k)/N\).
This also proves the asserted absence of finite poles.

For \(1\le k\le N/2\), Taylor's formula for the two entire factors
in (15) gives
\[
 |N\epsilon_{N,k-1}(u)-2(u-\pi ik)|
                 \le C_R k^2/N,\qquad
 \left|\frac1{N\epsilon_{N,k-1}(u)}
            -\frac1{2(u-\pi ik)}\right|\le C_R/N .
 \tag{17}
\]
For the first bound use \(|u-\pi ik|\le C_R k\):
the exponential correction is \(O(k^2/N)\) and the hyperbolic-sine
correction is \(O(k^3/N^2)\). Their arguments remain in a fixed
compact set. Dividing by the two lower bounds (16) proves the second.

On this lower half, the difference of the shift coefficients in
\(B_N\) and \(B\) is consequently bounded by
\[
 C_R\,|T_{N,k-1}-\tau_{k-1}|/k
                           +(C_R/N)|T_{N,k-1}|.
 \tag{18}
\]
Its sum is \(O_K(N^{-1})\) by (14). On \(N/2<k<N\), (16) and
the exponential tails (14) bound the sum of both coefficient
magnitudes by \(C_K2^{-N/2}\). The remaining infinite tail
\(k\ge N\) is bounded the same way. This proves the first term
of (11); (13) proves its second term.
The exact diagonal products (5),(9) and (14) prove the other two.
No upper-endpoint denominator was replaced by a low-index limit.

All parameter-dependent trace-class series converge normally on
compact sets in the stated domain. Prove (11) on a slightly larger
compact polydisc about each point of \(K\), still inside \(|u|<\pi\).
Applying the Cauchy integral formula to the coefficient errors and
summing their absolute values proves every fixed derivative bound.
Finite coverings handle a general compact \(K\).
These are the actual scaled meridian derivatives:
\(\partial_u=(M/N)\partial_M\), with the full Leibniz rule retained.
They are not derivatives moving the root \(Q_N\).

## 5. Normalization and source scope

For real \(\lambda\ge0\) at \(u=0\), all \(\tau_r\) are nonnegative,
so there is an explicit trace norm:
\[
 \|B(0,\lambda)\|_1
   =\frac1{2\pi}\sum_{a\ge1}p_a(\lambda)
                      \sum_{k=1}^{a}\frac1k
   =\frac1{2\pi}\int_0^\lambda\frac{1-e^{-t}}t\,dt .
 \tag{19}
\]
At zero the integrand has its removable value one.
To verify the last equality, differentiate the absolutely convergent
Poisson series. If \(H_a=\sum_{k=1}^a1/k\), its derivative is
\(\sum_a p_a(H_{a+1}-H_a)
 =\sum_a p_a/(a+1)=(1-e^{-\lambda})/\lambda\).
The series vanishes at \(\lambda=0\).

Equations (5)--(11) retain the full finite cut and its endpoint current.
They also imply \(O_K(N^{-1})\) error when the four trace-class
operators in (11) are paired with any uniformly operator-bounded
family of tests. No such bound for an arbitrary growing knot
exterior is supplied by this boundary theorem. Differentiating (6)
retains derivatives of that exterior and every other original factor.

## 6. An exponentially accurate finite window with its boundary current

There is a stronger approximation when the exact finite coefficients
are retained. For \(2\le m\le N\), censor the cut law at \(m-1\):
\[
 \begin{split}
 P_N^{[m]}&=\sum_{a=0}^{m-2}p_{N,a}|a\rangle\langle a|
       +\left(\sum_{a\ge m-1}p_{N,a}\right)|m-1\rangle\langle m-1|,\\
 B_N^{[m]}&=-\sum_{r=0}^{m-2}
       \frac{T_{N,r}}{N\epsilon_{N,r}}|r+1\rangle\langle r|.
 \end{split}
 \tag{20}
\]
Both are supported on indices \(0,\ldots,m-1\).
The last mass is explicit, not discarded. Direct multiplication gives
\[
 [D_N,B_N^{[m]}]=P_N^{[m]}-P_0,\qquad
 \operatorname{Tr}P_N^{[m]}=1 .
 \tag{21}
\]
At real \(0\le\lambda/N\le1\) it is still a positive probe.
For the original unmarked scalar, its evaluation is therefore
unchanged exactly, at every \(m\); this fact is the old normalized-cut
identity. Every marked comparison instead retains (21)'s exact
defect. For \(m=1\), one may set \(P_N^{[1]}=P_0,B_N^{[1]}=0\).

Uniformly on compact parameter sets as in (11),
\[
 \begin{split}
 &\|P_N-P_N^{[m]}\|_1+\|B_N-B_N^{[m]}\|_1\\
 &\quad+\|D_N(B_N-B_N^{[m]})\|_1
       +\|(B_N-B_N^{[m]})D_N\|_1
                \le C_K(C_K/m)^m .
 \end{split}
 \tag{22}
\]
The same statement holds for every fixed parameter derivative.
The limiting operators have the identical censored construction
and estimate, with \(D_u\) and their already specified products.

Here is a direct proof with no real-probability assumption.
For \(|\lambda|\le L\), the original finite coefficients and their
Poisson limits obey
\[
 |p_{N,a}|,\ |p_a|
                  \le e^L L^a/a!.
\]
Use \(\binom{N-1}{a}\le N^a/a!\) and
\(|1-\lambda/N|^{N-1-a}\le e^L\) for the finite bound.
The probability error in (22) is at most
\(2\sum_{a\ge m}|p_{N,a}|\).
The current and both product errors are bounded, using (16), by
\(C_K\sum_{r\ge m-1}|T_{N,r}|
 \le C_Ke^L\sum_{a\ge m}(a+1)L^a/a!\).
For \(m>2L+2\), this last sum is bounded by a constant times
\(mL^m/m!\). The elementary inequality
\(m!\ge(m/e)^m\), obtained by integrating \(\log t\), proves (22)
after increasing \(C_K\). The finitely many smaller \(m\) are
absorbed in that constant. The same proof applies to the limit.
Buffered Cauchy estimates give the derivative assertion.

Consequently, for any fixed \(c>0\), the rank window
\[
                m_N=\lceil cN/\log N\rceil=o(N)
 \tag{23}
\]
has error at most \(e^{-cN+o(N)}\) in (22), uniformly on compact
parameter sets and for every fixed jet. It is understood for
sufficiently large \(N\), so \(2\le m_N\le N\).
This exponential accuracy uses (20)'s exact finite-\(N\) coefficients.
Replacing them by the limiting Poisson coefficients gives only
(11)'s algebraic error.

For a specified original marked cut matrix satisfying
\(\|C_N\|\le e^{C_\Gamma N+O(\log N)}\), choose
\(c>C_\Gamma+A\), with \(A>0\). Trace duality and (21) then give
\[
 \begin{split}
 |\operatorname{Tr}((P_N-P_N^{[m_N]})C_N)|&=O(e^{-AN}),\\
 |\operatorname{Tr}((B_N-B_N^{[m_N]})[C_N,D_N])|
                                                   &=O(e^{-AN}).
 \end{split}
 \tag{24}
\]
The second trace equals the first by the exact commutator identity,
not by deleting a cutoff current.
At the original complete root, this applies to fixed literal
crossing/cup/cap diagrams with polynomially bounded marks and their
standard framing/cut lines, or other explicitly bounded external
factors of at most exponential growth. Indeed [P] gives
\(\|R_N^{\pm1}\|_{\rm ph}\le20^{N-1}\) in the same orthonormal
physical head basis. Its cups, ordinary caps, marked cap and pivots
have polynomial norm, so a fixed finite tensor contraction has a
bound of the required form. Fixed crossing powers may be expanded
into their finitely many signed crossings.
For a micro-meridian family of exteriors, (24) and its fixed jets
require that exterior bound on the corresponding buffered compact
parameter set; no uniform exterior estimate is inferred from (11).
The full source can still have cancellations far below this
absolute error, so (24) is not a scalar relative-error assertion.

## 7. Coverage and the boundary of the conclusion

The scalar Poisson approximation is classical; see
[Le Cam's primary paper](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-s.pdf)
for coverage. The independent generating-function proof here also
handles compact complex \(\lambda\). [G] already supplies a bulk
conditioned-Poisson Gaussian presentation of the finite cut.
The additional statement here is trace-class convergence of the
entire actual endpoint Ward current, its products with \(D_u\),
and its fixed micro-meridian jets.

This result neither evaluates \(F_N\) nor identifies the internal
geometric centralizer chain. It does not project away Fourier aliases,
replace the marked source by a positive trace, or suppress any
source-current term. No geometric coefficient or volume lower bound
is inferred from the endpoint model.

## Complete chosen texts

All four complete matching texts were read. Their exact finite
source conventions are retained; all limiting estimates are proved above.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| I, direct | [Actual fixed-cut Ward source](research_fixed_interior_cut_source.md), 214 lines | 93b2887527e0b5c9cb93f4da77702c996f0524e0a93f0c0032909345efdbd1b2 |
| S, direct | [Binomial cut and exact marked current](research_binomial_cut_framing_density.md), 364 lines | 4bc6efc595fd6d59c0bc572d83495fb779cff230ff1cb9c14429a0b7c6a2a1b0 |
| P, direct for (24)'s complete-root application | [Uniform physical source costs](research_conway_uniform_physical_quartic.md), 477 lines | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| G, coverage | [Finite two-mode Gaussian and bulk Poisson source](research_soft_cut_two_mode_gaussian_source.md), 345 lines | 1f95717e33e0fdcfe6b1cd453a02b4e5e63d83ed578df761a5c8bdd07e990c19 |

Only written mathematics, text reads and hashes were used.
No mathematical program, numerical test, build, git operation,
earlier-final edit or public-manuscript change was made.
