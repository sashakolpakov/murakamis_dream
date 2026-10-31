# Actual Frobenius endpoint periods and the normal current correction

Research proof and independent audit, 27 October 2026. The actual
paired Frobenius source has an explicit Serre-dual relative interval
with the required geometric endpoints. Its original whole quantum
source gives a rational relative-period deformation of this interval.
The normal connection required by that deformation is computable;
it is already different from a naive divided-Borel generator at
first order. Endpoint norm growth is also explicit.

This is a source-level relative-period map. It does not identify
the full braid network's residual Gaussian currents with it.

## 1. The canonical interval is an actual finite unipotent source

Use the actual Sym^N source and dual from
[the marked Borel construction](actual_unprojectivized_frobenius_borel_torsor.md).
Write
\[
 \psi_\alpha=\alpha^N\sum_{k=0}^N v_k,\qquad
 \lambda_m(v_k)=\alpha^{-N}\binom Nk
       \left(\frac{1+m}{2}\right)^{N-k}
       \left(\frac{1-m}{2}\right)^k .                 \tag{1}
\]
The source pairing is one. These formulas include the missing
finite-u chart point m=-1 (u=infinity); no inverse flag coefficient
is introduced there.

Take D=0 in the framing map, so
\[
 s=C\alpha^2,\quad r=(1+m)/2,\quad
 A=(1+s)^{-1},\quad \tau=r/s=\frac{1+m}{2C\alpha^2}.
\]
The geometric marked interval tau=0 to 1 has the EXACT endpoints
\[
              m_0=-1,\qquad m_1=-1+2C\alpha^2.       \tag{2}
\]
Put L=C alpha^2 and n=h+f-e, where e,f,h are the original root
divided Frobenius matrices. Direct calculation in the actual module
gives
\[
 n\psi_\alpha=0,\quad n^{N+1}=0,\quad
 \partial_m\lambda_m=\tfrac12\lambda_m n,
 \quad\lambda_\tau=\lambda_0\exp(\tau L n).          \tag{3}
\]
Equivalently,
\[
 \lambda_\tau(v_k)=\alpha^{-N}\binom Nk
              (L\tau)^{N-k}(1-L\tau)^k .            \tag{4}
\]
Thus the interval co-source is a specified finite expression,
\[
 \mathcal I=\int_0^1\lambda_\tau\,d\tau
       =\lambda_0\sum_{j=0}^N\frac{(Ln)^j}{(j+1)!},
 \qquad \mathcal I Ln=\lambda_1-\lambda_0.           \tag{5}
\]
No inverse of n is used. Every original matrix insertion B satisfies
\[
 \mathcal I[Ln,B]\psi_\alpha
           =(\lambda_1-\lambda_0)B\psi_\alpha.       \tag{6}
\]
This retains both endpoints and their alpha-dependent displacement.
Since Omega_cut=d tau wedge dlog A, integrating its source kernel
along this marked interval gives precisely the co-source (5) times
dlog A, with that orientation. An arbitrary translation tau_0(A)
moves both endpoint rows; it does not erase them.

At L=1, the beta integral in (4) gives
\[
                  \mathcal I(v_k)=\frac{\alpha^{-N}}{N+1}.
                                                               \tag{7}
\]
For alpha=C=1 this is the original uniform Frobenius co-source.
Thus exponential endpoint norms do not imply an exponential scalar
period: the full integrated row, including cancellations, matters.

## 2. Serre residue preserves the same actual endpoint rows

Use the exact convention
\[
 v_k\longmapsto\binom Nk z^k\in H^0(\mathbb P^1,O(N)),
 \quad c_\lambda(z)=\sum_{k=0}^N
                   \frac{\lambda(v_k)}{\binom Nk}z^{-k-1}.
\]
The second expression is a Cech representative for
H^1(O(-N-2)); its pairing is Res_(z=0) c_lambda f dz.
These conventions and all actual normal operators are developed in
[the global Frobenius Cech source](global_frobenius_cech_source_and_endpoints.md).

For the interval (4) the representative is explicitly
\[
 c_\tau(z)=\alpha^{-N}\sum_{k=0}^N
                  (L\tau)^{N-k}(1-L\tau)^k z^{-k-1}. \tag{8}
\]
It is polynomial in tau, has the fixed allowed Cech exponents,
and retains both endpoints in (2). Residue, interval integration,
and the finite matrix action commute exactly. Hence (5)--(6) hold
as Serre-dual cohomology identities, not only scalar coincidences.
The residue pairing alone supplies no identification of n with the
network's full actual Hopf-adjoint current.

## 3. An original whole-source rational period retains ALL normal jets

Fix a residue string s of the original high integral color. Let
F_s(q), E_s(q) be its actual divided matrices, with the original
root sign included in E_s, so their root values are f,e. Write
\[
 B_k(q)=[\exp F_s(q)v_0]_k,\qquad
 A_k(q)=[v_0^*\exp E_s(q)]_k .
\]
The exponentials are finite because these matrices are strictly
triangular. Their root values are B_k=1 and A_k=binom(N,k).
Define original whole source and homogeneous dual
\[
 \begin{split}
 \psi(q)&=\alpha^N\sum_k B_k(q)v_k,\\
 \widetilde\lambda(q,m)(v_k)
    &=\alpha^{-N}A_k(q)
           ((1+m)/2)^{N-k}((1-m)/2)^k,\\
 U_s(q,m)&=\widetilde\lambda(q,m)\psi(q),\qquad
 \lambda(q,m)=\widetilde\lambda(q,m)/U_s(q,m).        \tag{9}
 \end{split}
\]
These are the actual divided-source germs, expressed homogeneously;
the normalization is their ACTUAL pairing. No root binomial weight
is differentiated in place of that pairing. In particular
\[
                       U_s(q_N,m)=1                 \tag{10}
\]
for every finite m, including both endpoints.

Consequently the whole interval co-source
\[
       \mathcal I_s(q)=\int_0^1
                 \lambda(q,-1+2L\tau)\,d\tau        \tag{11}
\]
is a rational relative-period integral on the tau line with the
zeros of U_s deleted and endpoints 0,1 retained. For fixed N it is
analytic near q_N on a small neighborhood where the compact path
has no U_s zero. Equivalently it exists coefficientwise in the
completed actual quantum normal ring. Every coefficient of the
inverse of U_s is polynomial in m because its constant coefficient
is one; normal expansion and the compact interval integral commute.
The same applies to its Serre representative (8), replacing lambda
by (9), and to every original whole matrix insertion B(q).

For each finite normal truncation this is an explicit algebraic
calculation followed by a relative rational period. It imposes no
uniform-in-N neighborhood, metric bound, or geometric-saddle claim.
It is generally a period, rather than a rational function of q:
integrating a rational row with moving poles can produce logarithms.

There is also an exact source-pair current connection. Put
\[
 P_0=\psi_0\lambda_0(\tau),\quad P_q=\psi(q)\lambda(q,\tau),
 \quad G=\psi(q)\lambda_0+(I-P_q)(I-P_0).
\]
Its root is I, so it is an invertible rational germ; directly
G psi_0=psi(q) and lambda(q)G=lambda_0. Define
\[
 K_q=G(Ln)G^{-1}-(\partial_\tau G)G^{-1}.            \tag{12}
\]
Since psi(q) is tau-independent, the exact identities are
\[
 K_q\psi(q)=0,\quad\partial_\tau\lambda(q)=\lambda(q)K_q,
\]
and for every insertion, including tau-dependent ones,
\[
 \partial_\tau[\lambda(q)B(q,\tau)\psi(q)]
    =\lambda(q)([K_q,B]+\partial_\tau B)\psi(q).      \tag{13}
\]
Integration gives the ACTUAL endpoint rows with all normal
coefficients retained. Formula (12) constructs a source connection;
it does not assert that the network's Hopf current equals K_q.
That comparison requires an actual intertwining calculation.

## 4. A literal actual first-normal defect forbids the naive lift

The distinction in the last sentence is already necessary at
N=3, r=3, residue string s=1 of the original high color 12.
Use epsilon=log(q/q_3), q_3=exp(pi i/3), and include the actual
root sign tau=(-1)^(Nr-1)=+1 in e(q). Direct integral Gaussian
coefficient differentiation gives
\[
 e(q)=e+\gamma\epsilon e+O(\epsilon^2),\quad
 f(q)=f+\gamma\epsilon f+O(\epsilon^2),\qquad
                 \gamma=1-2q_3=-i\sqrt3.           \tag{14}
\]
For example the first divided coefficient is, including its
constant beta sign, [4]_q/[1]_q; the sign does not affect its
logarithmic derivative, which at q_3 is
3(q_3+q_3^{-1})/(q_3-q_3^{-1})=gamma.
The remaining entries give the same gamma, as the exact audit
checks independently using integral Gaussian polynomials.

The naive whole divided generator
\[
             n(q)=[e(q),f(q)]+f(q)-e(q)
\]
therefore satisfies
\[
 n(q)\exp(f(q))v_0
             =-2\gamma\epsilon f\psi_0+O(\epsilon^2)\ne0. \tag{15}
\]
Indeed psi_1=gamma f psi_0,
n_1=gamma(2h+f-e), [n,f]=-2f-h, and n psi_0=0.
This proves (15) without numerical approximation. The endpoint
current (12) kills the actual whole source; hence it differs from
L n(q) already in this first normal. The extreme residue strings
s=0 and s=N-1 have vanishing first derivative here, so testing
only them misses the defect. This is a source/connection defect,
not a claim about failure of the actual quantum-group relations.

## 5. A sharp endpoint metric obstruction and its limitation

The actual root Frobenius coherent metric in this divided basis is
g_k=binom(N,k). Then
\[
 \|\psi_\alpha\|^2=|\alpha|^{2N}2^N,\qquad
 \|\lambda_m\|_*^2=|\alpha|^{-2N}
                         ((1+|m|^2)/2)^N.
\]
Thus the normalized rank-one source coupon satisfies EXACTLY
\[
                 \|\psi_\alpha\lambda_m\|
                               =(1+|m|^2)^{N/2}.     \tag{16}
\]
Any translated geometric interval of length one at fixed s has
endpoint displacement m_1-m_0=2s. The triangle inequality gives
max(|m_0|,|m_1|)>=|s|, hence
\[
 \max_{j=0,1}\|\psi_\alpha\lambda_{m_j}\|
                           \ge(1+|s|^2)^{N/2}.      \tag{17}
\]
At the regular anchor s=-2,A=-1 this is at least 5^(N/2), for
EVERY translation of the marked interval. The unshifted endpoints
are m=-1,-5, giving 2^(N/2) and 26^(N/2).

This rules out an automatic tame UNITARY endpoint comparison in
the specified actual Frobenius coherent metric. It does not rule
out the integrated period or cancellations: (7) is an exact
counterexample to that inference. A transported metric, a contour
comparison, or retained character compensation needs its own
proof. Neither Serre duality nor a root Borel isomorphism supplies
that proof by itself.

[The exact audit](../experiments/audit_actual_frobenius_relative_endpoint.py)
checks the finite unipotent/interval identities, Serre residues,
the actual integral Gaussian first-normal defect, and the metric
formulas. No volume asymptotic is assumed.
