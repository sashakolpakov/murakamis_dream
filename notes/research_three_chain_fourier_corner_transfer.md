# Restoring the original vertex at a Fourier boundary

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The corner deletion used in the Fourier analysis must be estimated
after the boundary has been specified. A bound for two ordinary
boundary colors is unnecessarily large when one boundary is a
Fourier variable. Here the exact transformed cardinal vector gives
a smaller bound on the entire horizontal Fourier period. In
particular, it permits the full first-attachment asymptotic to be
transferred from the retained vertex to the original vertex.

## 1. The transformed boundary vector

Use the original matrices and cardinal functions of
[the traced-vertex calculation](research_traced_three_vertex_endpoint.md),
Sections 1--2 and 7. Put
\[
 A=JM^3,\quad H=M^*M,\quad
 \widetilde A=A-E_L,\quad
 D_N=\kappa^{-1}ME_LM^{-1},\quad
 Y_*={\log2\over2\pi},\quad
 c=2\mathcal J(5/6),\quad M_\infty={4G\over\pi}.
 \tag{1}
\]
Here \(G\) is Catalan's constant, \(L=\lfloor N/50\rfloor\),
and \(E_L\) is exactly the removed square of transformed indices.
Thus
\[
 MAM^{-1}=\kappa H,\qquad
 M\widetilde A M^{-1}=\kappa(H-D_N),\qquad
 \|D_N\|\le CN^a e^{3N/25}.
 \tag{2}
\]
The last estimate is proved in Section 7 of the cited note. All
norms below are Euclidean vector or operator norms.

**Lemma 1.** Uniformly for real \(\xi\),
\[
 \|Mh(\xi+iY_*)\|\le CN^a e^{N\log2/2}.
 \tag{3}
\]
For every fixed nonnegative integer \(b\) and every real \(h\),
\[
 \|\partial_y^b Mh(\xi+i(Y_*+h))\|
 \le C_bN^{a_b}e^{N(\log2/2+\pi|h|)}.
 \tag{4}
\]
Both parities are included.

*Proof.* Write \(Q=e^{2\pi i/N}\), \(q=e^{\pi i/N}\),
\(Y=e^{2\pi iy}\), and
\(c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N)\).
The exact finite binomial identity in the cited note gives
\[
 (Mh(y))_j=\kappa c_y(-q)^j
       {Y^j(Q^{-1};Q^{-1})_j\over(Y;Q^{-1})_{j+1}}.
 \tag{5}
\]
On the line in (3), \(|Y|=1/2\). The uniform endpoint factorial
bound and the smooth denominator Riemann sum therefore bound each
entry by a polynomial in \(N\) times the exponential of
\[
 N\left\{{\log2\over2}+\mathcal J(s)+s\log(1/2)
                  -I(s,\xi)\right\},\qquad s=j/N,
 \tag{6}
\]
where
\[
 I(s,\xi)=\int_0^s\log|1-\tfrac12e^{2\pi i(\xi-u)}|\,du,
 \qquad
 \ell(s)=\int_{-s/2}^{s/2}\log|1-\tfrac12e^{2\pi iu}|\,du.
\]
The interval-minimization argument in
[the global modulus proof](research_three_vertex_global_wire_bound.md),
equation (5), gives \(I(s,\xi)\ge\ell(s)\).
Put \(a(s)=\mathcal J(s)+s\log(1/2)-\ell(s)\).
It is continuous on \([0,1]\), has \(a(0)=0\), and
\[
 a'(s)=\log{\sin(\pi s)\over\sqrt{5/4-\cos(\pi s)}}\le0,
 \quad
 \sin^2(\pi s)-(5/4-\cos(\pi s))
                    =-(\cos(\pi s)-1/2)^2.
 \tag{7}
\]
Thus (6) is at most \(N\log2/2\). Summing the squared
component bounds changes only the polynomial factor, proving (3).
This argument includes \(j=0\) and the full index range.

Every component of \(Mh(y)\) has frequencies
\(k-(N-1)/2\), \(0\le k<N\). Fourier coefficient extraction
on the line \(\Im y=Y_*\) bounds each vector coefficient by
the supremum in (3). Moving the line by \(h\) multiplies each
coefficient by at most \(e^{\pi(N-1)|h|}\); differentiating
\(b\) times costs at most \((\pi N)^b\). Summing the \(N\)
coefficients proves (4). At even levels the frequencies are
half-integral, but their differences are integral, so the same
coefficient extraction and estimate apply. \(\square\)

## 2. An error estimate with the original ordinary boundary retained

Let \(v(\zeta)=(e_0(\zeta),\ldots,e_{N-1}(\zeta))^T\)
be the original Newton evaluation vector. Choose any fixed word
\(A_1\cdots A_m\), with each \(A_j\) either \(A\) or
\(\widetilde A\), and define
\[
 R_{m,N}(\zeta,y)=v(\zeta)^T
                 (A^m-A_1\cdots A_m)h(y).
 \tag{8}
\]

**Theorem 2.** For each fixed \(m\ge1\) and fixed ordinary
derivative orders \(a,b\),
\[
 \sup_{\zeta\in[-2,2],\ \xi\in\mathbb R}
 |\partial_\zeta^a\partial_y^b R_{m,N}(\zeta,\xi+iY_*)|
 \le CN^B e^{Nr_m},\qquad
 r_m=(2m-2)c+{M_\infty\over2}+{3\over25}+{\log2\over2}.
 \tag{9}
\]
At \(\zeta=-2\cos(u+iv)\), with \(u,v\) real, and
\(y=\xi+i(Y_*+h)\), add \(|v|+\pi|h|\) to the exponent.
No sign or positivity of the observed scalar is assumed.

*Proof.* In the similarity (2), a telescoping difference of words
has at most \(m\) terms, each containing one \(D_N\) and
\(m-1\) factors chosen from \(H,H-D_N\). Since
\(\|H\|\le Ce^{2cN}\) and \(3/25<2c\), its norm is at most
\[
                  CN^B e^{N\{(2m-2)c+3/25\}}.
 \tag{10}
\]
The remaining vectors are \(v(\zeta)^TM^{-1}\) and \(Mh(y)\).
At every physical value and first normal, the exact inverse-crossing
identity and full Newton-vector bounds in
[the positive-cycle proof](research_positive_three_crossing_cycle.md),
equations (42)--(43), give
\[
 \|(v^TM^{-1})^{(\nu)}(c_j)\|
                    \le CN^B e^{NM_\infty/2}.
 \tag{11}
\]
Here \(\nu=0,1\) at a double root and only \(\nu=0\) at
the odd simple root. Full Hermite interpolation has polynomial
norm on the real color interval. Applying it to this vector-valued
polynomial extends (11) to every \(\zeta\in[-2,2]\).
Markov's inequality gives each fixed higher ordinary derivative.
Together with (3), (10) proves (9).

For the complex-color assertion, apply Bernstein--Walsh to the
ordinary-color polynomial of degree at most \(N-1\), after its
fixed ordinary derivatives. The extra factor is at most
\(e^{(N-1)|v|}\). Apply (4) at the Fourier boundary. This proves
the stated exponent, including all original normal data and both
level parities. \(\square\)

## 3. Consequence for the first complete-cap attachment

The exact cardinal identity \(N\int h(x)h(x)^T\,dx=I\)
holds on every horizontal period. With the original complete cap,
it gives
\[
 \begin{split}
 N\int W_N(x,u)\widetilde V_N(x,y)\,dx
    &=v(-2\cos u)^TA(A-E_L)h(y),\\
 \mathcal B_N(u,y)&:=v(-2\cos u)^TA^2h(y).
 \end{split}
 \tag{12}
\]
The difference is exactly
\[
 v(-2\cos u)^TAE_Lh(y)
       =\kappa^2(v(-2\cos u)^TM^{-1})H D_N Mh(y).
 \tag{13}
\]
Theorem 2 therefore applies to this deletion without also deleting
the cap. For \(m=2\), its rate satisfies
\[
 r_2<{17\over10}< {19113\over10000}-\frac15.
 \tag{14}
\]
For an explicit check, use
\(c<161533/500000\), \(G<11/12\),
\(\pi>157/50\), and \(\log2<347/500\). They give
\[
 r_2< {161533\over250000}+{275\over471}
                         +{3\over25}+{347\over1000}<{17\over10}.
 \tag{15}
\]
The bound on \(c\) is the calibrated dilogarithm bound used in
the global modulus proof. The Catalan bound follows already from
a finite upper partial sum of its alternating series; the checker
records it with the other strict constants.

Consequently any full retained-attachment asymptotic with the
[certified first-attachment action](research_three_cap_first_attachment.md)
transfers, with the same nonzero leading coefficient, to
\(\mathcal B_N\). The error (14) is exponentially smaller.
The strict margin persists near \(u=0,y=x_*\), with fixed
ordinary outside derivatives and Fourier derivatives. This deduction
requires the full retained integral in (12); a restricted Gaussian
integral alone would not suffice. It makes no claim about the
complementary contours for longer chains.

## 4. A larger deleted corner for a larger source domain

The argument does not require the particular cutoff \(N/50\).
For a fixed \(0<\epsilon<1/2\), let
\[
 L_\epsilon=\lfloor\epsilon N\rfloor,\qquad
 E_\epsilon=M^TP_{L_\epsilon}JM P_{L_\epsilon}M,\qquad
 \widetilde A_\epsilon=A-E_\epsilon.
 \tag{16}
\]
For sufficiently large levels \(2L_\epsilon\le N-1\), so
this is exactly the square of transformed indices
\(0\le i,j\le L_\epsilon\) in the same finite vertex.
The two elementary estimates in the original corner proof give
\[
 \|M^{-1}P_{L_\epsilon}\|
     \le CN^a{(N/2)^{L_\epsilon}\over L_\epsilon!},\qquad
 \|P_{L_\epsilon}JM P_{L_\epsilon}\|
     \le CN^a 2^{2L_\epsilon}.
 \tag{17}
\]
They use respectively \(2\sin(\pi r/N)\ge4r/N\) for
\(r\le N/2\), and the sine-binomial bound. The function
\(s\log(2e/s)\) increases on \((0,1/2)\); hence
\[
 \|\kappa^{-1}ME_\epsilon M^{-1}\|
      \le CN^a e^{N\sigma_\epsilon},\qquad
 \sigma_\epsilon=\epsilon\log(2e/\epsilon).
 \tag{18}
\]
Whenever \(\sigma_\epsilon<2c\), Theorem 2 holds with
\(3/25\) replaced by \(\sigma_\epsilon\), and with each
retained factor replaced by \(\widetilde A_\epsilon\).

In particular, for \(\epsilon=1/40\),
\[
 \sigma_{1/40}={\log80+1\over40}<{27\over200}<2c.
 \tag{19}
\]
The mixed ordinary/Fourier error for two vertices then has rate
less than \(343/200=1.715\), still more than \(19/100\)
below the certified first-attachment action. This statement bounds
the effect of the larger deletion; it does not assert a source
asymptotic on a larger domain.

For two ordinary boundary colors, use instead the original right
vector bound \(\|Mv^{(b)}\|\le CN^a e^{N(c+M_\infty/2)}\).
The corresponding full-source error for any fixed word has rate
\[
                (2m-1)c+M_\infty+27/200.
 \tag{20}
\]
Corollary 5 of the original traced-vertex proof gives the geometric
lower rate \((2m-1)c+M_\infty+3/25+1/15\). Their difference is
\[
                    {3\over25}+{1\over15}-{27\over200}
                       ={31\over600}>{1\over20}.
 \tag{21}
\]
Thus the larger corner is still negligible after the actual
complete-ended chain contraction, with both parities and all fixed
ordinary derivatives. A later source proof may use this larger
corner if needed to enlarge its holomorphic parameter domain;
the retained finite function must then be specified as
\(\widetilde A_{1/40}\), rather than silently changing the
cutoff in an earlier theorem.

## 5. Reproduction

Run `python3 experiments/check_three_chain_fourier_corner_transfer.py`.
The checker verifies the exact axis identity and the rational and
outward scalar budgets. The original finite binomial, physical
normal, and matrix identities are the proved inputs cited above.
