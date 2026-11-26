# A resummed reduced Markov matrix and the source spectral bound

Private written proof, 18 November 2026.

The actual prefix quotient has a universal calibration that distinguishes
its matrix norm from its prescribed source. After two positive Markov
stabilizations, an entry of the fully multiplied reduced matrix is an
exact Gaussian binomial. Some diagonal entries grow exponentially,
although the original zero-framed source is exactly one. This calculation
already includes cancellation in the intermediate transfer sum. Positive
diagonal changes of metric cannot remove these diagonal entries.

There is also a corrected, basis-independent upper bound. On the actual
common-meridian collar, the central source kernel bounds the source by
a polynomial times the largest spectral radius of the reduced Cartan
blocks. This does not identify that spectral radius with a geometric
action or assert a sharp volume bound.

The complete directs are R, the actual reduced braid source, and E,
the literal finite Euler factor. Every additional calculation is below.

## 1. The original matrix and its normalization

Fix
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,
 \qquad x=-q^{-1}.
 \tag{1}
\]
For \(0\le j<N\), put
\[
 f_j=\prod_{r=1}^j(1-Q^r),\qquad
 s_j=|f_j|=\prod_{r=1}^j2\sin(\pi r/N),\qquad f_0=s_0=1.
 \tag{2}
\]
Use the original balanced occupation basis, declared orthonormal for
the norm assertions. The literal positive checked crossing is
\[
 R_+=\kappa\,\mathsf P D\Theta,\qquad
 D_{a,b}=x^{-a-b}Q^{ab},\qquad
 \Theta=\sum_{n=0}^{d}
       \frac{(-1)^nq^{n^2}}{f_n}(\mathcal E_1F_2)^n .
 \tag{3}
\]
At completeness E gives
\[
 \mathcal E w_a=(Q^{-a}-1)w_{a-1},\qquad
 Fw_b=(1-Q^{b+1})w_{b+1},\qquad
 H_j:=\prod_{r=1}^j(Q^{-r}-1)=q^{-j(j+1)}f_j.
 \tag{4}
\]
The vacuum and top arrows remain their actual zero arrows.

On three heads consider the universal positive Markov word
\(W=R_2R_1\), with the rightmost factor acting first. R's actual
reduction gives the matrix on the two remaining heads
\[
 B=\mathcal B_3(W)
   =\kappa R_+S_2D_{\rm red},\qquad
 S_2=\sum_{n=0}^{d}\frac{(x^{-1}L_1F_2)^n}{f_n},
 \tag{5}
\]
\[
 D_{\rm red}w_a=\delta_a w_a,\qquad
 \delta_a=(-1)^aQ^{a(a-1)/2}x^{-2a}
          =(-1)^a q^{a(a+1)} .
 \tag{6}
\]
In (5), \(R_+\) includes one \(\kappa\); the other is displayed.
The original positive Markov scalar is
\[
 \alpha=\kappa x^{1-N}.
 \tag{7}
\]
Thus the actual zero-framed reduced matrix for this word is
\(\widehat B=\alpha^{-2}B\).
No new source or scalar normalization is introduced.

The original source of the one-head identity is one. Applying R's
exact pivotal Markov identity twice therefore proves
\[
          \Phi_0(W)=\alpha^2,\qquad
          \Phi_0(\alpha^{-2}W)=1 .
 \tag{8}
\]
This is a universal presentation operation, evaluated before any
asymptotic estimate. It is not a proposed family of knot cases.
The proof retains the original highest cut and both tail pivots.

## 2. The entire reduced matrix coefficient

The only possible outputs from input \((a,b)\) in (5) are
\[
 (c,e)=(b+l,a-l),\qquad
       0\le l\le\min(a,d-b).
 \tag{9}
\]
For such an output, the transfer \(n\) in \(S_2\) and the transfer
\(l-n\) in \(R_+\) satisfy \(0\le n\le l\). These are exactly
the original finite support conditions: every intermediate head lies
between zero and \(d\). There are no omitted endpoint terms.

The \(S_2\) coefficient is
\[
 (S_2)_{(a-n,b+n),(a,b)}
             =x^{-n}\frac{f_{b+n}}{f_bf_n}.
 \tag{10}
\]
Multiplying it by the literal coefficient (3), with its Cartan
factor evaluated after the uncheck transfer, gives
\[
 \begin{split}
 B_{(b+l,a-l),(a,b)}
 ={}&\kappa^2\delta_a x^{-a-b}Q^{(a-l)(b+l)}
               \frac{f_{b+l}}{f_bH_{a-l}}\\
 &\quad{}\times
 \sum_{n=0}^l
  \frac{x^{-n}(-1)^{l-n}q^{(l-n)^2}H_{a-n}}
       {f_nf_{l-n}} .
 \end{split}
 \tag{11}
\]
All factors in this identity precede absolute values.

At the complete root, substitution of (1) and (4) reduces its sum to
\[
 (-1)^lq^{l^2-a(a+1)}
 \sum_{n=0}^l
       Q^{n(a-l+1)}\frac{f_{a-n}}{f_nf_{l-n}}
   =(-1)^lq^{l^2-a(a+1)}\frac{f_{a-l}}{f_l}.
 \tag{12}
\]
Here is a finite proof of the last equality. For \(l<N\),
\[
 \sum_{k=0}^l {l\brack k}_Q(z;Q)_k z^{l-k}=1.
 \tag{13}
\]
The recurrence
\({l+1\brack k}_Q={l\brack k-1}_Q+Q^k{l\brack k}_Q\)
reduces the left side for \(l+1\) to the left side for \(l\):
after reindexing, the two factors are \(1-zQ^k\) and \(zQ^k\).
The initial value is one. All denominators used for \(l<N\) are
nonzero. Take \(z=Q^{a-l+1}\), set \(k=l-n\), and multiply
(13) by \(f_{a-l}/f_l\) to obtain (12).

Combining every phase in (11)--(12) gives the exact formula
\[
 \boxed{\;
 \widehat B_{(b+l,a-l),(a,b)}
 =x^{2d}\delta_a x^{-a-b}(-1)^l
       q^{\,2b(a-l)-l}\frac{f_{b+l}}{f_bf_l}.
 \;}
 \tag{14}
\]
All other matrix coefficients are zero. In particular,
\[
 \boxed{\;
 |\widehat B_{(b+l,a-l),(a,b)}|
                  =\frac{s_{b+l}}{s_bs_l}.
 \;}
 \tag{15}
\]
This is the coefficient of the actual multiplied matrix, not a sum
of absolute values of its unresolved paths.

For a diagonal entry \(l=a-b\), so it exists exactly when \(a\ge b\).
One may equivalently write its full phase as
\[
 \widehat B_{(a,b),(a,b)}
 =(-1)^a q^{\,a(a+1)+2b(b+1)+2}
                         \frac{f_a}{f_bf_{a-b}} .
 \tag{16}
\]
Indeed \(x^{2d}=q^2\). Equations (14) and (16) keep the original
Cartan, flip and zero-framing order.

## 3. An exponential diagonal, even after the transfer resummation

Define the continuous real function
\[
 \mathcal L(t)=\int_0^t\log(2\sin(\pi u))\,du,\qquad 0\le t\le1.
 \tag{17}
\]
Uniformly for \(0\le j<N\),
\[
                  \log s_j=N\mathcal L(j/N)+O(\log N).
 \tag{18}
\]
For completeness, on \([0,1/2]\) subtract
\(\log u\) from the integrand. The difference extends smoothly
to zero and has bounded derivative there; its Riemann-sum error
is bounded. The sum of \(\log(r/N)\) is
\(\log(j!)-j\log N\), whose difference from its integral is
\(O(\log N)\) by upper and lower rectangle sums for \(\log u\).
This proves (18) through the midpoint. For the other half use
\(s_d=N\), obtained by evaluating
\((X^N-1)/(X-1)\) at \(X=1\), and
\(s_{d-j}=N/s_j\). Reflection of the integral and its
\(O(\delta|\log\delta|)\) endpoint modulus give the same error.

The elementary integral identities are
\[
 \mathcal L(1)=\mathcal L(1/2)=0,\qquad
                  \mathcal L(1-t)=-\mathcal L(t).
 \tag{19}
\]
For example \(\int_0^\pi\log(2\sin u)\,du=0\) follows by
combining its two half-intervals with the double-angle formula;
reflection gives the second identity.

Take \(3\mid N\), \(a=2N/3\), \(b=N/3\). These are legal
physical occupations, including \(N=3\). Equations (15),(18) give
\[
 \log|\widehat B_{(a,b),(a,b)}|
       =N c_*+O(\log N),\qquad
       c_*=-3\mathcal L(1/3)>0.
 \tag{20}
\]
The strict sign needs no numerical value: on \([1/3,1/2]\),
\(\log(2\sin(\pi u))>0\), and \(\mathcal L(1/2)=0\).
Consequently
\[
 \liminf_{\substack{N\to\infty\\3\mid N}}
                   \frac1N\log\|\widehat B\|\ge c_*,
 \qquad
 \liminf_{\substack{N\to\infty\\3\mid N}}
          \frac1N\log\operatorname{Tr}(\widehat B^*\widehat B)
                         \ge2c_* .
 \tag{21}
\]
These statements hold despite the exact source value (8).

Every positive diagonal change of occupation metric leaves a diagonal
matrix coefficient unchanged. In the resulting orthonormal coordinates,
the operator norm is at least that coefficient's modulus. Thus (21)
also obstructs removing this growth by arbitrary positive diagonal
weights, even weights depending exponentially on \(N\). A unitary
Fourier transform leaves both norms in (21) unchanged.

This conclusion concerns the actual reduced matrix and the norm route.
It does not assert that a positive source-selected contraction is
impossible, or that the same excess is additive after attaching an
arbitrary exterior. No lower bound for an original knot invariant
is inferred.

## 4. A corrected source bound using spectral radii

This part again uses the whole common-meridian family at fixed \(q\).
Let \(m\ge2\), \(r=m-1\), and let \(W(M)\) be an actual analytic
total intertwiner, including whatever prescribed scalar framing
line its source convention requires. Put \(B(M)=\mathcal B_m(W(M))\).
In the remaining occupation basis,
\[
 K_{\rm r}(M)=M^rK_0,\qquad
 K_0^N=\varepsilon I,\qquad
       \varepsilon=(-1)^{(N+1)r}.
 \tag{22}
\]
The distinct eigenspaces \(U_a\) of \(K_0\) are fixed as \(M\)
varies. Since \(B\) commutes with \(K_{\rm r}\), it preserves all
these spaces. Let \(B_a=B|_{U_a}\), and let \(k_a\) be the
corresponding eigenvalue of \(K_0\), so \(|k_a|=1\).

R's exact source formula on the generic meridian set is
\[
 \Phi_0(W(M))=\sum_a h_a(M)\operatorname{Tr}B_a(M),
 \qquad
 h_a(M)=
 \frac{D_N(M)(M^mk_a-M^{-m}k_a^{-1})}
      {\varepsilon(M^{mN}-M^{-mN})},
 \tag{23}
\]
\[
             D_N(M)=\sum_{j=0}^{N-1}M^{N-1-2j}.
 \tag{24}
\]
The original finite source extends holomorphically through \(M=1\).
Its pole cancellation is retained; no individual \(h_a\) is
declared holomorphic there.

Fix sufficiently small \(\eta>0\), depending on \(m\), and assume
the actual family is analytic on a neighborhood of the closed disk
\(|M-1|\le\eta/N\). On its boundary,
\[
                |h_a(M)|\le C_{m,\eta}N
 \tag{25}
\]
uniformly in \(a,N\). To prove it, use the logarithm near one.
The quantity \(w=mN\log M\) has modulus between fixed positive
multiples of \(m\eta\), and is small when \(\eta\) is small.
Thus \(|M^{mN}-M^{-mN}|=|2\sinh w|\ge c_m\eta\).
The numerator factor involving \(k_a\) is bounded, and (24)
has modulus at most \(Ne^{C\eta}\).

For every finite matrix, including matrices with nontrivial Jordan
blocks, its trace is the sum of its eigenvalues with algebraic
multiplicity. Hence
\[
 |\operatorname{Tr}B_a|\le(\dim U_a)\rho(B_a),
 \tag{26}
\]
where \(\rho\) is the spectral radius. Apply (25)--(26) on the
circle and then the maximum principle to the actual holomorphic
source in (23). Since \(\sum_a\dim U_a=N^{m-1}\), this proves
\[
 \boxed{\quad
 |\Phi_0(W(1))|
 \le C_{m,\eta}N^m
       \sup_{\substack{|M-1|=\eta/N\\a}}\rho(B_a(M)).
 \quad}
 \tag{27}
\]
No choice of eigenvectors or condition number occurs in (27).
This is a basis-independent source estimate on the actual collar.
It is not a root-value-only estimate: discarding the collar would
discard the source's meridian normal information.

The estimate does not bound the displayed spectral radii or identify
them with representation volumes. In particular no such conclusion
is deduced from (20), from invertibility, or from a local critical
scheme. Quantum-normal derivatives are also outside this claim:
the entire argument holds at fixed root \(q\), with R's stated
common-meridian scope.

## Complete direct-source pins

* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.

Both complete directs were read nontruncated in the active sequence.
Their used implications have been checked. Older positive-source
and Markov-normalization notes were inspected for coverage; no
claim about their different energy models is imported here.
Only written mathematics and text/hash operations were used.
Frozen and public files are unchanged.
