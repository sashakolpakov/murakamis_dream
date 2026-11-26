# Original Kashaev state and complete ADO normalization: bounded critical-input audit

Date: 1 November 2026. Public checkout read at `2301771b66296cb7f2331938f1bfe0855719dd3d`.
The accompanying snapshot records the exact source hashes and reading extent. This is a mathematical dependency audit, not a volume proof or an audit of all linked results.

## 1. Conclusion and exact convention

The three requested notes use the actual finite Kashaev crossing and the phase-fixed enhanced convention, with one genuine reduced cut. I found no failure in their direct Fourier/gauge comparison, complete-color pairing, or complete modified-dimension normalization. The calculations below work for every integer level N>=2; no field of prime order, odd-level assumption, or nonzero quantum dimension is needed.

There is an essential convention distinction. Kashaev's 1995 paper makes the Nth power of its partition function invariant and allows an Nth-root phase from choices of the face data. The exact complex scalar used here is the enhanced convention recorded in Murakami–Murakami Section 4, with unknot value one. Its absolute value is the original Kashaev absolute value. It is inappropriate to assert a uniquely phase-fixed 1995 scalar without specifying this enhancement.

For a knot, the zero-framed reduced ADO family has complete value equal to that phase-fixed Kashaev scalar. For a c-component link, comparison with the specified total-writhe enhancement includes the sign (-1)^((N-1)(c-1)). Other explicitly recorded component-framing changes are unit phases. The full modified evaluation has exactly one further factor i^(N+3)/N, on the chosen cut component.

Two later literature displays need normalization care; direct definitions, rather than those comparison statements, were used. They are detailed in Section 8. The previously recorded literal inverse issue in the original paper was also checked at N=2. None supplies a counterexample to the Kashaev volume conjecture.

## 2. Primary sources and page conventions

1. R. M. Kashaev, *A Link Invariant from Quantum Dilogarithm*, arXiv:q-alg/9504020v1, 24 April 1995, <https://arxiv.org/pdf/q-alg/9504020v1>. PDF page 2 is printed page 1. Definitions are on printed pages 1–3, equations (2.1)–(2.17); the diagram partition and its invariant power are on printed pages 3–4, (3.1)–(3.6) and Theorem 1. The comparison with the earlier triangulated invariant is stated there for odd N, and is not imported for even N.
2. H. Murakami and J. Murakami, *The colored Jones polynomials and the simplicial volume of a knot*, arXiv:math/9905075v2, 10 June 1999, <https://arxiv.org/pdf/math/9905075v2>. PDF and printed page numbers agree. Page 3 gives the enhanced cut convention and s=exp(pi i/N); page 5 gives R_J; pages 10–14 give the four-index Kashaev crossing, scalar gauge and enhancement.
3. J. Brown, T. Dimofte, S. Garoufalidis and N. Geer, *The ADO Invariants are a q-Holonomic Family*, arXiv:2005.08176v1, submitted 17 May 2020, <https://arxiv.org/pdf/2005.08176v1>. PDF and printed page numbers agree. Pages 8–13, Section 2.1, supply the module, both dualities, R and inverse R, modified dimension and twist. The informal complete-color comparison is on page 18. The holonomicity and annihilator-ideal comparison theorems are not premises here.

The locally retained PDFs, their SHA256 hashes, and the exact downloaded URLs are in `primary-source-record.json`. Relevant pages were extracted as text; the potentially ambiguous displayed exponents were also inspected as rendered PDF pages. No assertion below rests on OCR alone.

## 3. Direct original-crossing Fourier calculation

Write d=N-1, omega=exp(2 pi i/N), s=exp(pi i/N), and p_j=product_(h=1)^j(1-omega^h). Every p_j for j<N is nonzero and p_d=N, by differentiating z^N-1 at 1. Also bar_p_j=(-1)^j omega^(-j(j+1)/2)p_j. These statements do not require N prime.

For Kashaev's original R-symbol with parameters (1,0,0,0), set

    u=[j-i-1], v=[i-l], t=[l-k], h=[k-j].

The two theta factors imply u+t<N and v+h<N. The sum of these four nonnegative residues is congruent to -1 modulo N and at most 2N-2, hence equals d. Conversely each composition of d and free index j reconstructs the original entry. Its coefficient is

    N omega^(1-(t+h)(u+h))/(p_u bar_p_v p_t bar_p_h).

With normalized Fourier matrix F_ij=omega^(ij)/sqrt(N), the free j-sum supplies the modulo-N conservation delta, including exactly the needed factor N to cancel the Fourier denominator. Putting z=t+h, the remaining exponent is

    1+c-z^2+z(a+b)+(c-z)u+(z-a)t.

Thus the two composition sums separate into S_(d-z)(omega^(c-z)) S_z(omega^(z-a)), where

    S_m(X)=sum_(j=0)^m X^j/(p_j bar_p_(m-j))
          =product_(j=1)^m(X-omega^j)/p_m.

The product identity follows by the finite coefficient recurrence (1-omega^m)S_m=(X-omega^m)S_(m-1). Its zeros force c<=z<=a. The remaining finite binomial sum is exactly the one displayed as (1.5) in the crossing note. If b+a-c>=N it contains 1-omega^N and is zero. Otherwise the output is (c,b+a-c) as an ordinary integer pair, and the coefficient is (1.1). This explicitly checks the potentially dangerous wrapped states; they were not omitted by an integer-conservation assumption.

The four-index enhanced definition in Murakami–Murakami page 10 is recovered by substituting (i,j,k,l)=(a,b,d,c) in the original symbol. In the repository's column-input/row-output convention this is B_K=P(R^o)^T, with P the tensor swap. The transpose must not be removed merely because a source describes its own index convention as P composed with R.

## 4. Quantum gauge, inverse and enhancement

On the complete color, H_j=d-2j, K=s^H, E v_j=[j]_s^2 v_(j-1), and F_low v_j=v_(j+1). Use the finite R with Cartan factor on the left:

    R^q=s^(H tensor H/2) sum_(k=0)^d
        s^(k(k-1)/2)(s-s^-1)^k/[k]_s! E^k tensor F_low^k.

The root lift s^(1/2)=exp(pi i/(2N)) is retained in the Cartan factor. In particular even N does not license resetting a square root separately on different entries.

For G_j=p_j/(1-omega)^j=s^(j(j-1)/2)[j]_s!, D_j=(-s)^j, and gamma=omega s^(-d^2/2), the direct equality is

    (F^-1 tensor F^-1)R^o(F tensor F)
      = gamma (DG tensor G) R^q (G^-1 tensor G^-1D^-1).

I checked the coefficient cancellation explicitly. On (a,b)->(c=a-k,b+k), the quantum coefficient before the diagonal factors is

    s^(H_c H_(b+k)/2+k(k-1)/2)
       (s-s^-1)^k/[k]! * ([a]!/[c]!)^2.

After conversion to p-factorials, the residual s-exponent differs from the desired expression by -N(b+c+k), and the residual (-1)-exponent by c-b-k. Since s^N=-1, their product is one. This retains the potentially exponential diagonal factorials exactly; no norm comparison of their condition numbers is used.

The inverse finite quantum sum has coefficients (-1)^k s^(-k(k-1)/2)(s-s^-1)^k/[k]! and the inverse Cartan factor on the right. Finite q-binomial cancellation and E^N=F_low^N=0 prove that this is the inverse. The negative Kashaev generator is obtained by inverting the exact gauge equality, not by assuming the literal printed inverse has the required phase.

For b strands the single staggered gauge

    U_b=F^(-tensor b) tensor_(j=1)^b(G^-1 D^(j-1))

works for all adjacent generators and their inverses, since each quantum generator conserves the integer weight sum. Its enhancement is exact:

    mu_q=K^-1, alpha_q=s^((N^2-1)/2),
    mu_K=-s S, alpha_K=-s, beta_q=beta_K=1,
    U_b mu_q^(tensor b)U_b^-1=mu_K^(tensor b),
    gamma alpha_q=-s.

Here F^-1 diag(omega^j)F=S and s^-d=-s. The positive and negative weighted partial traces are scalars because they intertwine E,F,K; their endpoint entries contain only one term and give alpha_q and alpha_q^-1. Thus gamma^w cancels the writhe correction for any signed braid word. The usual positive/negative braid and ribbon identities remain the underlying tensor-category construction; this audit checked the finite matrix, inverse, intertwining and enhancement identities relevant to the comparison, rather than re-proving the general framed-tangle functor theorem.

## 5. Reduced cuts, links and every pivotal turn

Closing any set of braid heads with the actual pivot preserves the intertwining property. For the K-pivot convention, ordinary partial trace of the E coproduct commutator gives commutation with E on the retained heads. For F, K-conservation and trace cyclicity yield

    Tr_last K_last[A,K_prefix^-1 F_last]=0,

so tracing the full F coproduct commutator gives commutation with the retained F. K is immediate. Iteration does not use the number of link components. Since K has N distinct eigenvalues and every internal F arrow is nonzero, the final cut endomorphism is scalar. This is elementary irreducibility at every N, not semisimplicity of the whole root category.

Consequently all closed-factor conjugations cancel under trace, and the remaining open-factor conjugation cancels by scalarity. The rank-one selected functional reads this scalar; it does not divide by the zero quantum dimension. This is why a badly conditioned G cannot introduce a hidden exponential normalization.

The complete primal/dual change is B v_j=(-1)^j s^(j(j-N))v_(d-j)^*. It directly intertwines the antipodes S(E)=-EK^-1 and S(F)=-KF, conjugates K^-1 to K and gives R^T=(B tensor B)R(B^-1 tensor B^-1). Thus the dual braid convention and primal source use the same reduced scalar.

For general x=q^alpha, Q=q^2, the direct pivotal note uses

    J_x v_a=(-x)^a Q^(a(a+1)/2) v_(d-a)^*.

Its dual color is x^-1 Q^-1, with the original unrolled H lift retained. The identity J_x^(-t)J_(dual x)=K^(1-N) is exact, and S^2 is conjugation by that pivot. The left/right evaluations and coevaluations are precisely those in BDGG (2.8), including K^(1-N) on the right evaluation and its inverse on the right coevaluation. Snake contractions cancel these inverse factors on their matched index. This checks the four turns; treating the turn as an unadorned transposition would not suffice.

In the balanced basis w_a=v_a/p_a, the product identity

    p_a p_(d-a)=N(-1)^a Q^(a(a+1)/2)

gives the actual cups and caps at the complete color x=q^d:

    p_ab=N x^(-b) delta_(a+b,d),
    ell_ab=x^a delta_(a+b,d)/N,
    m_ab=x^b/N^2.

The last expression is the unrestricted marked cap, not an ordinary cap with a support condition added. With psi_a=1, phi_a=1/N, e=psi phi and D=g^-1e, one has Tr(gDC)=Tr(eC) for every C, e^2=e, Tr(e)=1, and mp=1. There are k genuine cups, k-1 ordinary caps and one marked cap in the specified raw diagram, so the net scalar is exactly N^k N^(-(k-1)) N^-2=1/N. Balanced changes cancel on every internal wire by basis covariance. The separate face-character coefficient factor belongs to the homogeneous-source adapter and is not a second cut normalization.

Every auxiliary component is closed by the ordinary pivotal trace already present in L_N. No separate modified dimension or quantum-dimension denominator is inserted on those circles.

At completeness,

    g_ADO=K^(1-N)=(-1)^d K,
    theta_ADO=q^(-d^2/2)=(-1)^d alpha_q.

For a b-strand closure of writhe w with c components, w is congruent to b-c modulo 2. The ratio of the two specified enhancements is therefore (-1)^(d(b-1-w))=(-1)^(d(c-1)). It is one for knots, need not be one for links, and always has modulus one. Actual component framings must still be recorded; mutual crossings are not self-writhe.

## 6. The ADO family and its exact complete value

BDGG uses E v_j=[alpha-j+1]v_(j-1), F v_j=[j+1]v_(j+1). The nonzero diagonal change v_j(new)=[j]!v_j(old) gives exactly the repository's E=[j][alpha-j+1], F=1. The factor in BDGG (2.9) reduces by

    (q-q^-1)^(2k)/(q^k(q^-2;q^-2)_k)
      =q^(k(k-1)/2)(q-q^-1)^k/[k]!

to the finite R above. Thus this is the stated literature color, not a replacement inspired by the colored Jones polynomial.

In a zero-framed knot, the common Cartan term q^(w alpha^2/2) cancels with the quadratic part of theta_alpha^-w. The remaining crossing and pivotal entries are Laurent in x=q^alpha, with only nonzero fixed denominators [k]!, k<N. The reduced cut scalar is therefore Laurent in x; generic scalarity extends through its exceptional finite set by polynomial identities. At alpha=d it is the complete simple color, so the knot comparison in Section 5 gives exactly the phase-fixed Kashaev scalar.

From BDGG (2.17)–(2.18), the full one-cut state is the reduced scalar multiplied by

    d_N(alpha)=-q^(N(1-N)/2)
       (q^(alpha+1)-q^(-alpha-1))/(q^(N alpha)-q^(-N alpha)).

Set M=-q q^alpha=e^u, hence alpha=d+u/Log q, with Log q=pi i/N. The numerator is -2 sinh u and the denominator 2(-1)^d sinh(Nu). Thus, as a whole holomorphic germ at u=0,

    d_N(e^u)=i^(N+3) sinh u/sinh(Nu),
    d_N(1)=i^(N+3)/N.

Equivalently d_N(M)=i^(N+3)M^(N-1)/(1+M^2+...+M^(2N-2)). The retained peripheral polynomial evaluates to N at M=1. Its shift ratio is exactly -q^-1(q^2M^2-1)/(M^2-1); the pole in this localized ratio does not permit deleting the regular whole germ at M=1.

This proves |F_red|=|A_raw| and |N_full|=|A_raw|/N at this complete pointing, with the recorded unit framing character. It neither bounds the normalization on an arbitrary moving meridian region nor identifies a meridian derivative with a q-transverse derivative.

## 7. Finite diagnostics and their limits

The private `replay.py` calls the public constructors without calling their output-writing mains. Original four-index weights, Fourier transforms and quantum R matrices are built separately. The replay checked N=2,3,4,6,9 in finite fields with a primitive 4Nth root. It checked 31 actual cut braid words (knots and links, including nonzero multi-component examples) at N=2,3,4,6, and six 90-digit whole-dimension/twist evaluations at N=2,3,4,6,9,12. At N=2 the printed candidate-inverse countercheck was done exactly over Q, not in a finite field.

`finite-replay.json` gives each record. These tests check risky indexing and phases; the uniform conclusions rely on the derivations above. The floating-point germ tests are diagnostics of an already explicit algebraic identity. The replay shares local constructors with the public audits and is not an independently implemented second software library.

## 8. Precise literature normalization notices

**Quantum enhancement exponent.** Murakami–Murakami v2 p.3 defines s=exp(pi i/N). Its p.5 R_J at the last retained weight has a single diagonal partial-trace term: R contributes s^(d^2/2), and its displayed p.13 mu_J contributes s^d. The required scalar is therefore s^((N^2-1)/2). The tuple and Lemma 4.5 on p.13 instead display s^(N^2-1). This is a discrepancy under the paper's own s convention, not a rename between s and q=s^2. For N=2 the direct value is exp(3 pi i/4), whereas the latter display gives -i. The repository uses the direct partial-trace value, which also gives gamma alpha_q=-s and agrees with the enhanced Kashaev tuple on p.14. No conclusion here relies on the differing printed exponent.

**Full versus reduced ADO value.** BDGG v1 p.8 uses q=zeta_(2r)=exp(pi i/r). Its defining (2.17), p.12, and (2.18), p.13, give d_r(r-1)=i^(r+3)/r. The reduced unknot cut is one, so the full modified unknot is i^(r+3)/r. The informal Remark on p.18 says N_K^r(r-1) coincides with the normalized Jones/Kashaev value; that statement omits this scalar in the displayed normalization. The repository instead retains it and distinguishes full from reduced. This observation does not invoke or invalidate the source's separate holonomicity results.

**Literal original inverse.** Kashaev v1 printed p.3 (PDF p.4), (2.15)–(2.16), when combined with (2.12), gives product -I at N=2 by exact rational arithmetic. The tested further levels give omega I, but this audit does not promote those finite tests to an additional all-level inverse formula. The direct quantum inverse and exact positive-crossing gauge already supply the required actual inverse for the enhanced definition. Replacing a phase-ambiguous original negative-crossing representative changes only its recorded phase; it does not license ignoring phases inside a sum.

## 9. Remaining inputs and minor wording issue

The audited comparison closes the local crossing, enhancement, turns and complete one-cut normalization gate. It does not on its own prove the homogeneous face-resolvent formula for an arbitrary Morse diagram, the coefficient/grid reduction, the confluent Casimir normal functional, any saddle asymptotic, or a geometric volume identification. Those are separate mathematical inputs. The generic all-level annihilator, ordinary-color pointing beyond the complete color, and geometric A-factor assertions linked later in the pointing note were outside this bounded reading.

Likewise the 1994 triangulated Kashaev construction is not being used to extend an odd-level triangulation theorem to even N. The all-N object here is the finite enhanced braid/tangle state, with the precise original four-index comparison above.

A harmless wording precision remains in `actual_complete_augmented_source_normalization.md`, lines 86–87: “ENTIRE specified local meridian function” can be read as globally entire. The displayed sinh ratio is a holomorphic germ near u=0 and is generally meromorphic away from there. “whole specified local meridian germ” is unambiguous. The formula and its complete value are correct.

No new source-gap, filling, knot class or volume conclusion is inferred from this audit. No public mathematical file was edited during this reading.
