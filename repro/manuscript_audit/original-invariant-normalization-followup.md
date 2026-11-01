# Original invariant and complete normalization: bounded follow-up

Read at `2301771b66296cb7f2331938f1bfe0855719dd3d`, 1 November 2026.
The [snapshot](original-invariant-normalization-snapshot.json) records source hashes, primary-source versions and the finite replay scope.
This audit concerns the actual invariant definition and its normalization; it gives no volume conclusion.

## Convention and outcome

The three main sources are [the crossing comparison](../../notes/kashaev_crossing_and_period_lattice.md), [the ADO pointing](../../notes/kashaev_ado_pointing.md), and [the complete augmented normalization](../../notes/actual_complete_augmented_source_normalization.md).
Their direct local comparison and complete one-cut normalization check for every integer $N\ge2$, including even and composite levels.
The proof does not divide by the vanishing quantum dimension or estimate a diagonal gauge by its condition number.

The precise complex scalar is the **phase-fixed enhanced Kashaev convention**, with unknot value one.
Kashaev's original 1995 partition function allows an $N$th-root phase; its Theorem 1 makes the $N$th power invariant.
The enhanced convention fixes that phase and has the original absolute value.
This distinction matters for complex equalities, although it does not change the exponential absolute-value rate. See [Kashaev v1, printed pp. 3–4, (3.6) and Theorem 1](https://arxiv.org/pdf/q-alg/9504020v1), and [Murakami–Murakami v2, pp. 10–14](https://arxiv.org/pdf/math/9905075v2).

## Direct finite comparison checked

Put $d=N-1$, $s=e^{\pi i/N}$, $\omega=s^2$, $p_j=\prod_{h=1}^j(1-\omega^h)$, and $\bar p_j=\prod_{h=1}^j(1-\omega^{-h})$, with $p_0=\bar p_0=1$.
Let $R^o$ be Kashaev's original unbraided matrix (2.12), before the enhanced tensor swap.
All $p_j$, $j<N$, are nonzero; $p_d=N$.
The original four residues $u,v,t,h$ satisfy $u+t<N$, $v+h<N$ and $u+v+t+h\equiv-1\pmod N$, hence their sum is exactly $d$.
The free Fourier index supplies the conservation delta; the remaining sums use

\[
\sum_{j=0}^m\frac{X^j}{p_j\bar p_{m-j}}
 =\frac{\prod_{j=1}^m(X-\omega^j)}{p_m}.
\]

Its zeros remove every wrapped output, giving the ordinary integer conservation and coefficient (1.1) of the crossing note.
Substitution $(i,j,k,l)=(a,b,d',c)$ in the original four-index symbol identifies the enhanced matrix as $B_K=P(R^o)^T$, where $P$ swaps tensor factors and $d'$ here is an output index, not $N-1$.
This agrees with the literal four-index definition on Murakami–Murakami p. 10; dropping the transpose would change the convention.

For $G_j=p_j/(1-\omega)^j$, $D_j=(-s)^j$, and $\gamma=\omega s^{-d^2/2}$, direct factorial and exponent cancellation gives

\[
(F^{-1}\otimes F^{-1})R^o(F\otimes F)
 =\gamma(DG\otimes G)R^q(G^{-1}\otimes G^{-1}D^{-1}).
\]

Here $F_{ij}=\omega^{ij}/\sqrt N$, and $R^q$ is the explicit finite quantum matrix (2.1), including its Cartan factor with the fixed lift $s^{1/2}=e^{\pi i/(2N)}$.
The staggered tensor gauge (3.3) works for every adjacent generator and its actual inverse.
The enhancements satisfy

\[
\mu_q=K^{-1},\quad \alpha_q=s^{(N^2-1)/2},\qquad
\mu_K=-sS,\quad \alpha_K=-s,\qquad \gamma\alpha_q=\alpha_K,
\]

where $K v_j=s^{d-2j}v_j$ and $S v_j=v_{j+1\bmod N}$.
Thus the gauge factors and writhe factors cancel exactly in the reduced cut evaluation.
The inverse is supplied by the finite quantum inverse and this exact equality, rather than by assuming the phase of the printed candidate inverse.

## Turns, cut and component signs

Write BDGG for Brown, Dimofte, Garoufalidis and Geer, *The ADO Invariants are a q-Holonomic Family*.
The actual module in [BDGG v1, pp. 8–10](https://arxiv.org/pdf/2005.08176v1) becomes the repository module by the nonzero basis change $v_j^{\mathrm{new}}=[j]_s!v_j^{\mathrm{old}}$, where $[j]_s=(s^j-s^{-j})/(s-s^{-1})$ and $[j]_s!=\prod_{h=1}^j[h]_s$.
Its R coefficients, right pivot $g=K^{1-N}$, and both evaluations/coevaluations agree directly with the defining formulas there.
The explicit self-duality map and $J_x^{-t}J_{x^{-1}s^{-2}}=K^{1-N}$ in [relative pivotal duality, §§1–2](../../notes/relative_pivotal_duality.md) retain the unrolled lift and both right-turn factors.
Snake contractions cancel the pivot and inverse pivot on their matched indices; a bare transpose is not used as a turn.

Partial trace of the coproduct intertwining identities leaves an endomorphism commuting with $E,F,K$, regardless of the number of link components.
Distinct $K$-weights and nonzero internal lowering arrows force this cut matrix to be scalar at every $N\ge2$.
This cancels the gauge on the open factor as well as those on the traced factors.

With $e=\psi\phi$, $\psi_a=1$, $\phi_a=1/N$, the original selected mark is $D_{\mathrm{cut}}=g^{-1}e$ and
$\operatorname{Tr}(gD_{\mathrm{cut}}C)=\operatorname{Tr}(eC)$.
The balanced cups, ordinary caps and unrestricted marked cap are respectively

\[
p_{ab}=Nx^{-b}\delta_{a+b,d},\qquad
\ell_{ab}=x^a\delta_{a+b,d}/N,\qquad m_{ab}=x^b/N^2,
\quad x=s^d.
\]

Their specified raw contraction has net scalar $1/N$, with $mp=1$, and no further cut factor.
Every auxiliary circle uses its ordinary pivotal trace already in $L_N$; it receives no separate modified dimension.
See [the direct turn/source calculation, §§1–2 and 6–7](../../notes/quantum_bridge_cap_source.md).

At completeness $g_{\mathrm{ADO}}=(-1)^dK$ and $\theta_{\mathrm{ADO}}=(-1)^d\alpha_q$.
For a braid with $b$ strands, writhe $w$, and $c$ components, $w\equiv b-c\pmod2$; hence the ratio of these specified enhancements is $(-1)^{d(c-1)}$.
It is one for knots, but need not be one for links. Recorded component-framing changes supply only their explicit unit phases; mutual crossings are not self-writhe.

## Whole modified dimension and literature conventions

At fixed $s$, let $M=-s\,s^\alpha=e^u$, so $\alpha=d+u/\log s$.
The defining modified dimension, [BDGG (2.17)–(2.18), pp. 12–13](https://arxiv.org/pdf/2005.08176v1), gives

\[
d_N(e^u)=i^{N+3}\frac{\sinh u}{\sinh(Nu)},\qquad
d_N(1)=\frac{i^{N+3}}N.
\]

This is the whole holomorphic germ at $u=0$, generally meromorphic away from that neighborhood.
Let $A_{\mathrm{raw}}$ be the original marked tensor contraction, $F_{\mathrm{red}}$ its reduced zero-framed evaluation with the same marked component, and $\mathcal N_N$ the full one-cut modified ADO evaluation.
There is exactly one such factor on the marked component. Therefore $|F_{\mathrm{red}}|=|A_{\mathrm{raw}}|$ and $|\mathcal N_N|=|A_{\mathrm{raw}}|/N$ at this pointing, with the stated framing convention.
It is not a generic moving-meridian norm estimate or a claim about derivatives transverse to the root in $s$.

Two normalization discrepancies were checked against the primary definitions rather than used as premises:

- **Quantum enhancement:** Murakami–Murakami v2 p. 3 defines $s=e^{\pi i/N}$. Its p. 5 $R_J$ and p. 13 $\mu_J$ give a last-weight partial trace $s^{d^2/2}s^d=s^{(N^2-1)/2}$. The tuple and Lemma 4.5 on p. 13 instead display $s^{N^2-1}$. The repository uses the directly computed half exponent. This is not a rename between $s$ and $s^2$.
- **Full versus reduced ADO:** BDGG v1 p. 8 uses $q=e^{\pi i/r}$. Its defining (2.17)–(2.18) give full modified unknot $i^{r+3}/r$, whereas the reduced unknot is one. The informal comparison on p. 18 omits that scalar in this normalization. The repository retains it explicitly.

Separately, Kashaev v1 printed p. 3 (PDF p. 4), (2.15)–(2.16), combined with (2.12), gives product $-I$ at $N=2$ by exact rational arithmetic.
The actual inverse used above avoids this printed phase discrepancy; further finite tests are not treated as an all-level proof of a replacement inverse formula.

## Checked scope and remaining dependencies

The bounded replay separately constructs original weights and quantum matrices at $N=2,3,4,6,9$; it also checks 31 knot/link cuts at $N=2,3,4,6$, and six 90-digit whole-germ diagnostics through $N=12$.
See the public [crossing audit](../../experiments/audit_kashaev_crossing.py) and [normalization audit](../../experiments/audit_actual_complete_augmented_source_normalization.py).
These are supplementary checks; the uniform assertions above use the finite identities, not the samples.

The general framed quantum-tangle construction is the underlying definition. This reading checked its particular matrices, inverse, intertwining, enhancement, turns and cut comparison; it did not re-prove every general ribbon-category identity.
The homogeneous Morse face adapter, grid extraction, confluent Casimir normal functional, analytic noncancellation and geometric volume calibration remain separate proof inputs.
The later all-level operator and A-factor claims linked by the pointing note were not audited here.
In particular, neither the odd-only 1994 triangulated comparison nor a Jones volume statement substitutes for these inputs.
No unresolved local normalization obstruction was found; no claim about a full source gap or a new volume family follows from this audit.

After this reading, the complete-normalization note's phrase “ENTIRE specified local meridian function” was changed to “whole specified local meridian germ”; no formula changed.
The snapshot preserves the audited baseline hash and records this precision edit separately with its before/after hashes.
