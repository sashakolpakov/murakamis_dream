# Bidiagonal transport of full neighboring-height frames

24 November 2026. Written research proof.

The neighboring-height frame in P has an exact first-order update on each parity of the physical height grid. The update retains all \(N\) coordinates. A binomial estimate controls its accumulated full Gram, including every coherent cross term, at subexponential cost across any \(o(N)\) height steps. This is a simplification of the actual source coefficients, not an evaluation of the global quartic minimum.

## 1. Full frames and the specified source

Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and \(\sqrt q=e^{\pi i/(2N)}\). All fractional phases below mean these exponentials. For \(0\le j\le d\), put
\[
 \alpha_j=(j+\tfrac12)\pi/N,\quad
 \lambda_j=2\sqrt q\cos\alpha_j=q^{j+1}+q^{-j},\quad
 \mu_j=\sin\alpha_j,\quad
 F_a=(Q;Q)_a=\prod_{h=1}^a(1-Q^h).
\]
The empty product is one. Use P's complete continuants
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)=(\lambda+qQ^a\sigma)D_a
                              -q(1-Q^a)^2D_{a-1},
\]
\[
 (U_s)_{aj}=q^{-a}D_a(\lambda_j;\lambda_s)/F_a,
 \qquad 0\le a,j,s\le d.
 \tag{1}
\]
Here \(U_s\) means \(U_{\lambda_s}\) of P, not a truncation of that matrix. It is invertible. In coefficient coordinates let \(Ze_a=e_{a+1}\) for \(a<d\) and \(Ze_d=0\), with \(e_a\) the standard orthonormal basis. Thus \(Z^N=0\) and its counting operator norm is one.

The specified height gauge and source are
\[
 f_j=e^{i\pi j(j+1)/(4N)},\quad
 S=\operatorname{diag}((-1)^j\mu_j/f_j),\quad
 W_s=U_sS,\quad G_s=W_s^\dagger W_s.
 \tag{2}
\]
The matrix \(G_s\) is the pullback of the coefficient counting metric. It is not identified with the earlier positive height metric \(G_{\rm ht}\). For a vector \(x\), write \(\|x\|_{G_s}^2=x^\dagger G_sx\).

## 2. One physical height update

For \(0\le s\le N-3\), the exact full-frame relation is
\[
 A_s:=U_{s+2}U_s^{-1}
   =(I+q^{-s-2}Z)(I+q^{s+1}Z)^{-1}.
 \tag{3}
\]
Every inverse here is its finite geometric sum modulo \(Z^N\). In particular
\[
 (I+q^{s+1}Z)U_{s+2}=(I+q^{-s-2}Z)U_s.
 \tag{4}
\]
Both multipliers are unit lower bidiagonal. This constructs every physical frame from \(U_0\) or \(U_1\) by linear solves, without discarding an endpoint coordinate. For \(N=2\), no such update is required.

For proof, define
\[
 \Phi_{\lambda,\sigma}(z)
       =\sum_{a=0}^dD_a(\lambda;\sigma)z^a/F_a.
\]
P(17)--(19) prove, modulo \(z^N\),
\[
 (1-\lambda z+qz^2)\Phi_{\lambda,\sigma}(z)
  =N_\sigma(z)\Phi_{\lambda,\sigma}(Qz),\qquad
 N_\sigma(z)=1+q\sigma z+q^3z^2.
\]
At the actual physical root \(\sigma=\lambda_s\), this numerator factors as
\[
 N_s(z)=(1+q^{s+2}z)(1+q^{1-s}z).
\]
The rational function
\[
 R_s(z)=\frac{1+q^{-s-1}z}{1+q^{s+2}z}
\]
has constant term one and satisfies \(R_s(z)N_s(z)=N_{s+2}(z)R_s(Qz)\) identically. The unique constant-one solution modulo \(z^N\) therefore gives \(\Phi_{\lambda,\lambda_{s+2}}=R_s\Phi_{\lambda,\lambda_s}\). Uniqueness uses only \(1-Q^a\ne0\) for \(0<a<N\), so includes composite \(N\). P's coefficient conversion substitutes \(z=q^{-1}Z\) into \(R_s\), proving (3). No top-degree boundary remainder occurs.

## 3. Accumulated cost for coherent packets

For \(k\ge1\) with \(0\le s<s+2k\le d\), set
\[
 A_{s,k}=U_{s+2k}U_s^{-1}
 =\prod_{j=0}^{k-1}
   (I+q^{-s-2-2j}Z)(I+q^{s+1+2j}Z)^{-1},\qquad
 D_{N,k}=2^k\binom{N+k-1}{k}.
 \tag{5}
\]
The quotient denotes commuting matrix multiplication and inversion. For \(k=0\), set \(A_{s,0}=I\) and \(D_{N,0}=1\). Then
\[
 \|A_{s,k}\|_2,\ \|A_{s,k}^{-1}\|_2\le D_{N,k},
\]
\[
 D_{N,k}^{-2}G_s\preceq G_{s+2k}\preceq D_{N,k}^{2}G_s.
 \tag{6}
\]
The order in (6) is the Hermitian positive-semidefinite order. It controls arbitrary complex coherent packets simultaneously. The same inequality holds for \(U_s^\dagger U_s\) before the \(S\) gauge.

To prove the bound, a product of \(k\) numerator factors has coefficient \(\ell^1\) norm at most \(2^k\). The coefficient of \(z^m\) in the inverse of the \(k\) denominator factors is a sum of \(\binom{m+k-1}{k-1}\) unit-modulus terms. Consequently its truncated coefficient \(\ell^1\) norm is at most
\[
 \sum_{m=0}^{N-1}\binom{m+k-1}{k-1}=\binom{N+k-1}{k}.
\]
Multiplication and truncation cannot increase the product \(\ell^1\) bound. For \(\sum_mc_mZ^m\), its operator norm is at most \(\sum_m|c_m|\). Interchanging numerator and denominator proves the inverse bound. Applying both bounds to \(W_sx\) proves the Gram comparison, with no omission of cross terms or replacement of a Gram matrix by the identity.

The elementary factorial estimate gives
\[
 \log D_{N,k}\le k\log\frac{2e(N+k-1)}{k}.
 \tag{7}
\]
Thus \(k=k_N=o(N)\) implies \(\log D_{N,k}=o(N)\), uniformly in the starting physical height. This uses \((k/N)\log(N/k)\to0\); multiplying a separate \(2N\) bound at every step would lose this improvement. In particular, arbitrary nonzero \(N\)-dependent coherent packets have the same leading logarithmic norm in these frames across \(o(N)\) same-parity steps. All statements concern the full \(N\)-dimensional frames, not selected spectral windows. They do not identify the two parity starting frames.

## 4. Source and original marked observation

P(11) fixes the source normalization exactly:
\[
 W_sf=q^{-d/2}e_d,\qquad \|f\|_{G_s}=1.
 \tag{8}
\]
Every \(A_{s,k}\) fixes \(e_d\). The full height-coordinate transport
\[
 H_{t\leftarrow s}=W_t^{-1}W_s,\qquad t=s+2k,
\]
satisfies \(H^\dagger G_tH=G_s\) and \(Hf=f\). In the same fixed metric \(G_s\), its norm and inverse norm are at most \(D_{N,k}\), since \(W_sHW_s^{-1}=A_{s,k}^{-1}\).

Only for the marked primitive \(\nu=c=1+q\), P(13)--(16) give the canonical mode row
\[
 \ell_s=v^{\mathsf T}W_s,\quad v_a=(-Q)^a,\qquad
 \ell_sf=\omega_N=i(-1)^{N-2}q^{-3/2}.
\]
Its exact dual norm and initialized angle are therefore
\[
 \ell_sG_s^{-1}\ell_s^\dagger=N,\qquad
 \frac{|\ell_sf|}{\|f\|_{G_s}\|\ell_s\|_{G_s^{-1}}}
       =\frac1{\sqrt N},\qquad
 \ell_tH_{t\leftarrow s}=\ell_s.
 \tag{9}
\]
Indeed \(v^{\mathsf T}\overline v=N\) and \(W_sf\) has only its last coordinate. The physical row is \(\beta_N\ell_s\), with \(\beta_N=(T_*/A_c)\kappa(1-q)/2\) and \(\kappa=q^{d^2/2}\); \(T_*\) and \(A_c\) are P's original boundary constants. Its dual norm is \(|\beta_N|\sqrt N\) and its initialized period is \(\beta_N\omega_N\). The original exterior \(\chi_N\) remains external. No physical row is silently normalized to unit residue.

## 5. Relation to the fixed-degree problem

Equations (4) are linear in the full packet coefficients. They compare frame columns, or \(U_sx\) and \(U_{s+2}x\) for one common vector \(x\); they impose no relation between independently summed physical height sectors. They may be retained as auxiliary linear equations when these frames are used; they introduce quadratic squared residuals rather than higher-degree products. Eliminating these constant-coefficient frame equations is a linear substitution and preserves polynomial degree. This does not identify the simple coideal module with the confluent Casimir algebra of the original Conway quartic compiler or remove its bilinear multiplication gates.

The initialized marked angle in (9) is polynomially small. After an arbitrary original short tangle, the direction and observed scalar can change. The comparison retains the source, cap, phases and full Gram; it does not bound that later marked angle below or compare the norm rate with hyperbolic volume. No fixed \(G_{\rm ht}\) metric bound, universal braid unitarity, or finite-exception theorem follows from this note.

## Complete input and coverage

The sole complete selected proof input is [P](research_coideal_normalized_marked_period.md), 410 lines, SHA256
\[
 \texttt{e5e7ab88016f682411258ccab299f4b7bc2ab6e7052366729d59d993abf84d4b}.
\]
P already gives the general Toeplitz neighbor comparison and exact source/mark transport. The refinement here is its explicit bidiagonal physical update, the full coherent Gram bound (6)--(7), and its stated pullback metric normalization. No novelty for binomial counting or pullback inner products is claimed.

Only written mathematics and text/hash operations were used. Earlier final notes, public manuscripts and the progress ledger remain unchanged.
