# A uniform Frobenius base for the source and its marked period

Research note, 26 October 2026. This places the actual scalar source
coefficients at all levels on one difference base, retaining the
Frobenius coordinate and root phases. A standard multiplicative-to-
additive group model resolves the quantum--meridian point. The
normalized two-channel source algebra extends there. A second marked
chart evaluates the original central-pole normalization as a whole.

The resulting Frobenius period is explicit and regular in h^2. This
is the universal root-center period, not the knot's selected Bloch
period. The global source comparison and volume conjecture remain
unproved.

## 1. Keep the Frobenius coordinate independent before restricting a root

Use the fixed literature parameter q_N=exp(pi*i/N) and meridian M.
Introduce independent coordinates q,M,w and the finite phase cover

    zeta^4=1, U=w^2,
    sigma(q)=q, sigma(M)=qM, sigma(w)=-w,
    sigma(zeta)=zeta.                              (1.1)

The actual root graph is

    Gamma_N: q=q_N, w=M^N, zeta=i^(1-N).           (1.2)

It is sigma-stable because q_N^N=-1. The phases are exactly

    zeta_N=q_N^(N(1-N)/2),
    epsilon_N=(-1)^N=-zeta_N^2,
    eta_N=i^(N+3)=zeta_N^3.

No phase is reset independently at a level. The coefficient field
on each phase component is C(q,M,w), with constant field

    C(q,U).                                      (1.3)

For a proof, sigma^2 fixes w and scales M by q^2. A rational
invariant in M cannot have a finite nonzero pole, since its
infinite q^2 orbit would also be poles. It is therefore Laurent
in M, and invariance forces all nonzero M exponents to vanish.
The remaining sigma invariance is w->-w, giving C(q,w^2).

Adjoining the shift T gives the exact relations

    TM=qMT, Tw=-wT.

Under (1.2), the second is the ordinary root identity
T M^N=q_N^N M^N T. Thus this base extends the literature
coefficient algebra and recovers it at each specified root.
It does not impose monodromy one on a quantum-A module.
Here w is a half-Frobenius meridian coordinate; it is not
the geometric longitude or the norm-torsor spectral variable.

The original normalization functions are now fixed rational functions:

    rho=q-q^(-1), f=M-M^(-1),
    d=zeta^3 f/(w-w^(-1)),
    C_cut=-zeta U/[(U-1)(U+1)],
    epsilon=-zeta^2,
    delta=rho(M^2-M^(-2)), nu=epsilon rho^2,
    A=epsilon rho(M+M^(-1))
                    *(qM^2-q^(-1)M^(-2))/(w+w^(-1)). (1.4)

They restrict to the actual full ADO dimension, cut line and
adjacent-source overlap. Direct substitution gives

    sigma(d)/d=-f(qM)/f(M), sigma(C_cut)=C_cut.

The central divisor U=1 and the half-root sign of w are retained.

## 2. Root graphs give a genuine algebraic rigidity test

On each fixed phase component, the union of Gamma_N for infinitely
many N in its residue class modulo four is Zariski dense.

Indeed clear denominators of a proposed identity and write

    P(q,M,w)=sum_(a,b) f_(a,b)(q)M^a w^b.

Let D_M be the span of its finitely many M exponents. If N>D_M,
the exponents a+Nb for distinct pairs (a,b) are distinct.
Restriction to Gamma_N is therefore zero only if every
f_(a,b)(q_N) is zero. Infinitely many distinct q_N force these
fixed polynomials to vanish. This proves the density assertion,
including complex coefficients and every phase component.

There is a finite-degree version over a number field K. After
clearing denominators let D_q be the q degree and D_M the M
exponent span. If

    N>D_M, phi(2N)>[K:Q] D_q,                    (2.1)

then an exact whole-graph identity at that one level proves
the generic identity on that phase component. The algebraic
degree of q_N over K is at least phi(2N)/[K:Q], so each
polynomial f_(a,b) has degree too small to vanish at q_N unless
it is zero. For K=Q(i), the sufficient bound is phi(2N)>2D_q.
The graph must lie in the domain of the cleared comparison.

The degree hypotheses are essential: w-M^N vanishes on a
single graph, and a cyclotomic polynomial vanishes at its q_N.
Neither satisfies the relevant strict bound. Checking only
M=1,w=1, or a few unspecified meridian samples, is not a
whole-graph certificate. The actual knot period is not assumed
to have this fixed rational presentation or these degree bounds.
The test concerns source coefficients and proposed algebraic
comparison maps once their bounds have been established.

## 3. The deformation group is an existing definition

The standard group scheme

    G^(lambda)=Spec R[t,1/(1+lambda t)]

is recalled in [Mezard--Romagny--Tossici, Section 1.2](https://arxiv.org/html/1104.2222v1#S1.SS2).
We use this definition with lambda=rho and M=1+rho*t. Its
group law and inverse follow directly by multiplying M:

    t*tprime=t+tprime+rho*t*tprime,
    t^(-1)=-t/(1+rho*t).                          (3.1)

For rho invertible it is G_m, while its rho=0 fiber is G_a.
This is existing group-scheme theory. Only the abstract and
this definition were consulted; no isogeny, extension, or
classification proof from that source is assumed here.

Symmetric source coordinates near M=1 are

    s=(M-M^(-1))/rho, c=M+M^(-1),
    c^2-rho^2 s^2=4, M=(c+rho*s)/2.              (3.2)

This is the selected c=2 chart of the same deformation, since
s=t(2+rho*t)/(1+rho*t). Its group law is

    (s,c)*(sprime,cprime)
      =((s cprime+c sprime)/2,
                       (c cprime+rho^2 s sprime)/2). (3.3)

Multiplication preserves the displayed norm; associativity
follows either by expansion or by the M multiplication law.
On the exceptional identity fiber rho=0,c=2 it becomes addition
of s. This resolves the ideal (rho,M-1) in the meridian chart.

The original meridian step is multiplication by (1,q+q^(-1)):

    sigma(s)=((q+q^(-1))s+c)/2,
    sigma(c)=(rho^2 s+(q+q^(-1))c)/2.             (3.4)

It preserves c^2-rho^2s^2 and has determinant one. Meridian
inversion is (s,c,w)->(-s,c,w^(-1)); direct multiplication
gives the relation inversion*sigma*inversion=sigma^(-1).
At the exceptional identity fiber the action is exactly

    sigma(s)=s+1, sigma(w)=-w.                   (3.5)

Charge is the ordinary multiplication map of this group.
For the cubic source it is (M,w)->(M^3,w^3), equivalently
s->s(c^2-1), c->c^3-3c. It intertwines the original meridian
step with the third source step, retaining the charge from
the actual projective source construction.

## 4. The normalized adjacent source extends over the exceptional fiber

Let p=q^(-1)M^2-qM^(-2), r=sigma(p), and k=q+q^(-1). On (3.2),

    p/rho=(k s c-(c^2-2))/2=:p_hat,
    r/rho=(k s c+(c^2-2))/2=:r_hat.               (4.1)

Their difference is c^2-2, a unit near c=2. Thus the old point
ideal (p,r) pulls back to the principal ideal (rho); its proper
transform has no residual point. This resolves the nonfree
rank-one factor (u,h) in the earlier cyclic source lattice.
The exceptional factor rho remains a specified line and divisor;
principalizing the ideal does not discard that source datum.

Normalize the source numerators by their recorded factor nu:

    d_hat=delta/nu=epsilon*s*c,
    a_hat=A/nu=c*r_hat/(w+w^(-1)).                (4.2)

Here epsilon^2=1 on the phase cover. These are regular on the
chosen chart with w+w^(-1) invertible. The two coefficient
matrices from the actual source become

    t_1_hat=[d_hat a_hat;0 0],
    t_2_hat=[0 0;a_hat d_hat].

On the exceptional identity fiber,

    d_hat=2 epsilon*s,
    a_hat=2(2s+1)/(w+w^(-1)).                    (4.3)

At s=0,w=1 their matrix-algebra generators have nonzero units:
a_hat=1 and a_hat^2-d_hat^2=1. Thus their multiplicity algebra
and local scalar comparison torsor extend over the joint
quantum--meridian degeneration. This resolves the shrinking
fixed-level unit in the preceding normal-form note. It is the
two-channel coefficient algebra that extends; the N-dimensional
color factor and full knot section have not been algebraized.
The original numerator matrices are exactly nu*t_i_hat on every
root graph. The original projectors are t_i_hat/d_hat, so this
normalization retains their full germs and defines no new state.

The full affine factor has the uniform expression

    (1+w^(-2))*a_hat/d_hat
                   =epsilon*w^(-1)*r_hat/s.      (4.4)

Its exceptional value is epsilon*w^(-1)(2s+1)/s. The pole at
s=0 and the central cap at w^2=1 stay in the relative model;
normalizing the numerators has not discarded either of them.
The earlier obstruction to a common lattice for both unscaled
projectors is consequently still present.

## 5. One marked Frobenius period realizes every prescribed root

Put h=Log q and retain the original Tate mark tau=pi*i,
so N h_N=tau. On the identity chart let

    u(h,s)=arsinh(s sinh h), M=exp(u),
    log w_per=(tau/h)arsinh(s sinh h).             (5.1)

This is the selected solution of M-M^(-1)=rho*s with M=1
at s=0. The quotient in (5.1) is regular at h=0, since u is
odd in h. More precisely

    log w_per=tau*s+tau*(s-s^3)h^2/6+O(h^4).

It is analytic in h^2 locally for bounded s. At h=h_N it is
exactly N Log M, so w_per=M^N as a whole germ. Translation
by q gives u->u+h, hence w_per->exp(tau)w_per=-w_per. Thus
this one period section respects the original meridian action
and recovers (1.2), rather than choosing unrelated sections
at different levels.

At the exceptional fiber it is the horizontal period

    dlog w_per=tau ds, w_per(0)=1,
    w_per=exp(tau*s).                             (5.2)

This is an algebraic line with connection and a marked horizontal
period, not a rational function of s. A regular algebraic group
homomorphism G_a->G_m is constant: its defining function is an
invertible polynomial, hence constant, and its identity value is
one. Thus the nonzero Tate marking cannot be replaced by an
algebraic character on the exceptional additive fiber. Retaining
the period comparison is necessary even though its coefficient
group and connection are algebraic.

All normalized scalar source formulas in (4.1)--(4.3), and the
source step (3.4), are even in h after this period section is
substituted on a fixed phase component. Indeed c=2sqrt(1+s^2
sinh^2 h), k=2cosh h, and w_per are all even in h. This parity
does not assert parity or regularity of the knot's geometric
exponential exp(S/h).

## 6. The pole normalization becomes a marked regular evaluation

The point s=0,w=1 alone does not evaluate d/rho: its expression
is zeta^3*s/(w-w^(-1)). Retain the second chart

    w=1+s*ell, ell invertible.                    (6.1)

Then the whole normalized dimension and cap are regular:

    d/rho=zeta^3*w/[ell(w+1)],
    s*C_cut=-zeta*w^2/[ell(w+1)(w^2+1)].          (6.2)

Their complete values are zeta^3/(2ell) and -zeta/(4ell).
The actual graph fixes the slope, not only the point:

    ell_N=(dw/ds)|_(s=0)=N rho_N/2.              (6.3)

Combining (6.2)--(6.3) recovers exactly

    d_N(1)=zeta_N^3/N.

On the uniform period section this slope is

    ell(h)=tau*sinh h/h,
    d(h,0)=zeta^3*h/tau.                         (6.4)

Thus the central normalization is a regular evaluation on a
marked chart, including its transverse root-graph direction.
No separate zero or pole was evaluated. At the exceptional
fiber ell=tau; the period marking fixes that value.

The meridian translates this marked chart to the other cap
charts. Its orbit is not a single invariant point; those arrows
remain in the lattice/source groupoid. This construction does
not make all adjacent projector arrows integral on one lattice.

## 7. Scope and verification

This supplies a uniform difference base for the actual source
coefficients, its standard group deformation, a regular normalized
two-channel algebra, and one marked Frobenius period with exact
root restrictions. It also gives an algebraic rigidity test for
bounded comparisons. These replace levelwise coefficient choices
by specified functions and period data.

The horizontal section above is the universal Frobenius period.
It is not the knot's marked Bloch regulator. An actual global
source/section comparison with the positive triangulation still
has to be constructed, with all matrix and lattice transitions.
The root-graph density theorem does not apply to an unknown
comparison without its fixed presentation and degree bounds.
The source coefficient algebra does not determine the scalar
coefficient of the geometric exponential in the selected period.

The subsequent [whole-period reconstruction](whole_period_cyclotomic_rigidity.md)
extends this root-only base by an independent v=q^N and t=1/N.
Its action is sigma(w)=vw, with commuting derivatives
D_q=q partial_q+t^(-1)v partial_v and
D_M=M partial_M+t^(-1)w partial_w. The slice v=-1 recovers
the base here but is not preserved by D_q. Thus quantum-normal
jets require this extension before specialization. Bounded mixed
jets then reconstruct any proposed fixed algebraic comparison,
including one on a marked etale shape cover. This does not
algebraize the full knot state or construct the missing map.

The [fixed central normalization theorem](algebraic_central_normalization.md)
controls a comparison factor once its fixed finite algebraic
presentation is proved. It does not supply that global comparison.
The volume conjecture remains unproved.

The subsequent [common Frobenius/regulator period space](common_frobenius_regulator_period_space.md)
now puts this Frobenius mark and the geometric regulator action
over one explicit logarithmic Heisenberg connection. Its additional
Tate period J recovers all four root phases; unlike a frozen phase
sheet it carries the q-direction connection. The full complete cap
is -i J h/(pi*i), and the geometric exponential retains its volume
term. Adjoining the rational Frobenius coordinate preserves an
existing nonsplit source class, by a Laurent-coefficient retraction.
Thus the common period space does not by itself supply the missing
actual source comparison.

[The audit](../experiments/audit_uniform_source_base.py) verifies
the group law, Weyl and meridian matrices, normalized source and
cap identities, and period-section translation through h^6.
Four phase sheets verify bounded-degree exponent separation
and cyclotomic factor degrees. Fourteen root levels verify the
original phases and marked complete normalization, with 28
generic scalar root-graph specializations. These are source-base
checks, not quantum-volume experiments.
[Results](../experiments/uniform_source_base_results.json).

Reproduce with:

    python3 experiments/audit_uniform_source_base.py
