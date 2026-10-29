# Rational Faddeev periods: folding, gluing support and polar cycles

Research note, 25 October 2026. This gives an exact multidimensional
period representative for the rational Gaussian--Faddeev integral class
already used in the state notes. It fixes the contour by construction.
It also proves why replacing that period by a sum over gluing solutions
needs a further polar-cycle theorem.

Garoufalidis--Kashaev,
[Evaluation of state integrals at rational points](https://arxiv.org/abs/1411.6062),
Section 2.1, gives the one-dimensional quasi-periodic folding method.
The multidimensional identities below are proved directly. Their stated
one-dimensional evaluation theorem is not assumed in higher dimensions.
This note does not claim a volume theorem for all alternating knots.

## 1. The exact finite translation data

Fix a positive integer n, delta=2pi i, omega=exp(2pi i/n), and the
audited meromorphic function

    F_n(z)=Phi_(1/sqrt(n))(z/(2pi sqrt(n))-c_b).

Use its exact equations

    F_n(z+delta)=F_n(z)/(1-exp(z/n)),
    F_n(z+n delta)=F_n(z)/(1-exp z).                    (1.1)

Let A be an integral symmetric d by d matrix, v_j integral columns,
epsilon_j integers, and rho,xi_j arbitrary parameters. Define

    f_n(z)=exp[i z^T A z/(4pi n)+rho^T z]
                         product_j F_n(v_j^T z+xi_j)^epsilon_j.
    t_i=exp z_i,  a_j=exp xi_j,  x_j=exp((v_j^T z+xi_j)/n).

For m>=0 put R_m(x)=product_(r=0)^(m-1)(1-omega^r x)^(-1);
define the negative m by the inverse translation recurrence. For
k in Z^d, direct substitution gives the rational finite-shift ratio

    r_k=f_n(z+delta k)/f_n(z)
       =exp[-k^T A z/n-pi i k^T A k/n+2pi i rho^T k]
                          product_j R_(v_j^T k)(x_j)^epsilon_j. (1.2)

The exponential of the linear z term is a monomial in exp(z_i/n).
The phase in (1.2) uses its stated analytic square-root convention;
it is not discarded as an unnamed power of omega. All ratios are
rational on the finite root cover after retaining their constant phases.
They satisfy r_(k+l)(z)=r_k(z)r_l(z+delta k) exactly.

The coarse n-step multiplier is

    H_i(t)=chi_i product_l t_l^(-A_il)
                  product_j(1-a_j t^v_j)^(-epsilon_j v_ji),
    chi_i=exp(2pi i n rho_i-pi i n A_ii).               (1.3)

Every H_i is invariant under all small translations delta e_l.
Nothing in (1.3) specializes a peripheral parameter or suppresses a
norm factor. The formulae hold at composite n as well. The previous
Heisenberg normalization theorems use odd n; folding itself does not.

## 2. This class contains the specified rational literature integrands

Take exactly the integrand from `general_annihilator_and_volume.md`,
with boundary variable t_0, internal variables t, Q_b=b+b^(-1):

    I_b=exp[pi i (t_0,t)^T H(t_0,t)+Q_b pi c^T(t_0,t)+C(b)]
          product_j Phi_b(v_j0 t_0+v_j,int^T t+i Q_b rho_j)^epsilon_j.

Here the H,c,v,rho data are rational and fixed as in that note. Choose
an integer L clearing the internal exponents so that
A=L^2 H_int,int and v'_j=L v_j,int are integral. At b^2=1/n set

    t=L z/(2pi sqrt(n)),
    rho'_n=L[(n+1)c_int/(2n)+i t_0 H_int,0/sqrt(n)],
    xi_j=2pi sqrt(n) v_j0 t_0+2pi i(n+1)(rho_j+1/2),
    C_n=C(b)+pi i H_00 t_0^2+Q_b pi c_0 t_0.

Then, with the literal scaled source contour Gamma_n,

    J_b(t_0)=exp(C_n) [L/(2pi sqrt(n))]^d
                              integral_(Gamma_n) f_n(z) dz. (2.1)

This is an exact change of variables, including its Jacobian. Additional
normalizations already attached to J remain attached. No alternative
solution of a quantum A-operator has been chosen.

For the literature peripheral coordinate Q=exp(-2pi b t_0), the
factor exp xi_j is

    a_j=Q^(-n v_j0) exp[2pi i(n+1)(rho_j+1/2)].          (2.2)

Rational powers require the same finite peripheral covers as in the
annihilator note. Equations (2.1)--(2.2) retain Q, n, all phases, and
the full generic peripheral factors. The central t values in this
change of variables are not held fixed along a semiclassical shape path.

## 3. Multidimensional folding with the source contour retained

Let T_i act by z->z+delta e_i, and N_i=1+T_i+...+T_i^(n-1).
Initially assume no H_i is identically one; see the regularized
specialization below for that case.
On the translation orbit of f_n, T_i^n=H_i. Since the H_i commute
with every T_l, the following is a pointwise meromorphic identity:

    K_n(z)=sum_(k in {0,...,n-1}^d) f_n(z+delta k)
                                      / product_i(1-H_i(t)),
    product_i(1-T_i) K_n=f_n.                          (3.1)

Its proof is the telescoping equality (1-T_i)N_i=1-T_i^n in each
coordinate. This uses the full unnormalized orbit sum; replacing it
by an average would introduce the missing factor n^d.

Consequently, wherever the indicated corner integrals exist,

    integral_Gamma f_n dz
       =sum_(e in {0,1}^d) (-1)^|e|
                               integral_(Gamma+delta e) K_n dz. (3.2)

Use the same orientation of dz_1 wedge ... wedge dz_d and the literal
scaled source Gamma in (2.1). There is no guess of a preferred Bethe
cycle in (3.2).

There is also a common-excision version when K_n has new poles on
one of those contours. Pull every corner back to Gamma, cut off the
same compact parameter domain, and excise the same neighborhoods of
the poles of all its corner terms. On that common domain (3.1) gives
equality exactly. At each fixed cutoff first remove the common
excisions, and then remove the cutoff as in the original integral.
This defines a
regularized alternating pairing equal to its value. The corner terms
must not be regularized independently. If their poles do not meet the
contours and the tails vanish, this reduces to the ordinary cubical
cycle with vertical caps removed at infinity.

The exact rational Faddeev identity factors f_n into algebraic cyclic
coefficients and the continuous Heisenberg/dilogarithm period. The
same is true of K_n because the finite r_k are rational. Thus
(K_n, the folded source contour with its matched excisions) is an
explicit period pairing for the chosen realization. It retains the
polar-cycle data that the unpointed finite boundary module omits.

If a coarse multiplier is identically one, introduce independent
auxiliary units u_i near one by multiplying f_n by
exp[sum_i Log(u_i)z_i/(n delta)]. Its coarse multipliers become u_i H_i,
so (3.1) applies generically. When the source has a holomorphic
exponential-moment germ, as proved for the charged state class in the
existing notes, the original period is the regular evaluation at u=1
of the whole folded pairing. Individual corner terms need not have a
regular value there. These are auxiliary moment parameters, not a
replacement definition of the quantum state.

## 4. The algebraic gluing support is a Koszul reduction

There is a precise algebraic reason that H_i=1 appears. Let R be a
coefficient ring containing the H_i and the required inverse monomials,
without inverting 1-H_i. On the free rank-n module V_i with basis e_j,
let T_i e_j=e_(j+1), with T_i e_(n-1)=H_i e_0. Then

    [V_i --(1-T_i)--> V_i]
          is chain equivalent to [R --(1-H_i)--> R].    (4.1)

For a direct proof, use source columns
e_0,...,e_(n-2),sum_j e_j, and target columns
e_0-e_1,...,e_(n-2)-e_(n-1),e_0. Both changes are unimodular.
The map becomes diag(1,...,1,1-H_i). Its unit summands are
contractible. No division by n or 1-H_i has been used.

Tensoring (4.1) gives a chain equivalence

    Koszul(1-T_1,...,1-T_d; tensor_i V_i)
          ~ Koszul(1-H_1,...,1-H_d;R).                 (4.2)

Concretely, write g_i=1-H_i. The degree-zero homology of the right
side is exactly R/(g_1,...,g_d), the ordinary algebra of the gluing
locus. If the g_i form a regular sequence, all its higher homology
vanishes, so the ordinary quotient suffices. Keeping the complex
retains the extra information when this regularity fails, for example
because some gluing equations are redundant. Singularity of the zero
set alone does not imply nonzero higher Koszul homology.

Thus Koszul is bookkeeping for the simultaneous constraints and their
relations, not an additional knot invariant or a construction of the
period torsor. In a regular neighborhood one may work directly with
the gluing quotient; the integration cycle and regulator data still
have to be supplied separately.

At H_i=1, in characteristic zero the average
n^(-d)product_i N_i is the projector to the joint invariant line.

The algebraic assertion does not imply that an ordinary noncompact
contour integral factors through these coinvariants. Moving a contour
can cross poles, and multiplying by an internal rational function can
introduce poles or destroy decay. In particular one cannot invert
1-H_i and then argue that the period vanishes. The cycle pairing and
its polar boundary are essential in this pushforward.

## 5. The local gluing-point residue and its regulator factor

Write chi_i=exp eta_i on a chosen logarithmic sheet and put

    W(z)=-(1/2)z^T A z+eta^T z
                                  +sum_j epsilon_j Li_2(a_j exp(v_j^T z)).

Then exp(partial_i W)=H_i and

    Hess W=-A+sum_j epsilon_j xcentral_j/(1-xcentral_j) v_j v_j^T,
    xcentral_j=a_j exp(v_j^T z).                        (5.1)

This is a uniform, symmetric logarithmic gluing Jacobian. Suppose p
is an isolated solution H_i=1, f_n is regular there, and det Hess W
is nonzero. The local Leray residue is exactly

    Res_p K_n dz
       =(-1)^d [sum_k f_n(p+delta k)]/det Hess W(p).    (5.2)

Indeed the derivative of (1-H_i) with respect to z_j is
-partial_i partial_j W at p. The residue convention is the integral
over increasing ordered arguments of (1-H_i), divided by (2pi i)^d.
Formula (5.2) fixes the Jacobian and its sign. Singular points need
the full local residue algebra rather than an inverse Hessian.

Here is the exact regulator content of a summand, without an n-limit.
For a logarithmic lift of p, write zeta_j=v_j^T z+xi_j,
w_j=Log(1-exp zeta_j), and choose integers k with

    -Az-sum_j epsilon_j v_j w_j+eta=2pi i k.

Choose eta=2pi i n rho-pi i n diag(A) literally, so that
rho=diag(A)/2+eta/(2pi i n). The continuous exponent in f_n from
the local rational formula is i S/(2pi n), where

    S=(1/2)z^T A z+sum_j epsilon_j[Li_2(exp zeta_j)+zeta_j w_j]-eta^T z.

At p the gluing equation gives

    S=sum_j epsilon_j[Li_2(exp zeta_j)+(1/2)zeta_j w_j]
                       -(1/2)eta^T z-pi i k^T z
                       +(1/2)sum_j epsilon_j xi_j w_j. (5.3)

The omitted algebraic prefactor is explicitly
exp(diag(A)^T z/2) product_j(1-exp zeta_j)^epsilon_j
                            /product_j D_n(exp(zeta_j/n))^epsilon_j.
Thus the critical-point term contains the Rogers/Heisenberg period,
cyclic coefficients, source/peripheral terms and the full Jacobian.
It is not just the Bloch norm or just a positive factorial weight.

## 6. A uniform source-pole cancellation criterion

The actual divisor orders can be derived without a zero/pole theorem
from the literature. F_n is holomorphic and nonzero in
0<Im z<2pi(n+1), by its defining integral. Iterating the n-step
equation (1.1) shows that its only zeros and poles are at z=delta ell,
ell in Z, and

    ord_(delta ell) F_n=-floor((ell-1)/n).              (6.1)

Indeed the points ell=1,...,n lie in the nonvanishing strip. A coarse
shift by n reduces the order by one, which proves the formula at
every other integer. Every point can be translated into the strip,
so there are no additional divisors.

Suppose all epsilon_j are positive. Let the source contour be the
horizontal plane z=x+i lambda with

    gamma_j=(v_j^T lambda+Im xi_j)/(2pi) in (0,n+1).

For the unit folding tube z=x+i(lambda+2pi s), s in [0,1]^d,
each orbit summand has total shifts k+s in [0,n]^d. Put
P_j=sum_i max(v_ji,0). Its local F_n pole order in this tube is
at most P_j: an encountered integer ell obeys

    ell<gamma_j+n P_j<n(P_j+1)+1,

so (6.1) gives floor((ell-1)/n)<=P_j. With multiplicity epsilon_j
the bound is epsilon_j P_j.

First assume distinct binomial divisors D_j:1-a_j t^v_j=0 have no
common component. At a generic point of D_j away from the remaining
zeros of 1-H_i, the order of H_i is
-epsilon_j v_ji. Thus product_i(1-H_i)^(-1) has a zero of order
epsilon_j P_j, which cancels the source pole of every orbit summand.
The same proof allows common components if all their v_j are positive
multiples of one primitive vector on that component; the orders then
add with the same signs. This is the polar coorientation condition.

Consequently K_n has no source-divisor poles in the folding tube,
away from its remaining 1-H_i divisors. The assertion is divisorial;
on the complement of the latter divisors, normality removes residual
codimension-two singularities. It is uniform in d,n and the number of
factors. It uses the strict strip inequalities, positive multiplicities,
and the stated coorientation, not a knot census.

Distinctness of the binomial components is a generic source/peripheral
condition when it is not forced to fail by the coefficient data. This
criterion is not asserted for every knot realization. Full peripheral
parameters must remain available when testing it. Even when source
poles cancel, a multivariate cycle-localization and tail argument is
still needed before summing only the common H_i=1 residues.

Independent auxiliary shifts xi_j -> xi_j+alpha_j make these binomial
components distinct generically, after factors with v_j=0 have been
retained as external scalars. For finitely many integral vectors,
coincidence of components is a finite set of algebraic relations
among the a_j. The generic shifted family therefore satisfies the
criterion whenever its source strip inequalities persist. If the
original charged integral has a holomorphic germ in those shifts,
its value is the regular specialization of the whole period. A gluing
point of the shifted family can meet the polar boundary in this
specialization; its period must not be discarded by evaluating only
the open gluing equations of the special fiber.

## 7. A Faddeev counterexample to automatic gluing-point localization

For any odd n consider the absolutely convergent period

    f_n(z)=exp(z/(2n))/(1+exp(z/n))=1/[2cosh(z/(2n))].

It is an exponential times a ratio of the literature functions:

    f_n(z)=exp(z/(2n))
        *Phi_b(z/(2pi sqrt(n))+i b/2)
         /Phi_b(z/(2pi sqrt(n))-i b/2),    b=1/sqrt(n).

The audited functional equation proves this identity. Nevertheless
H=f_n(z+n delta)/f_n(z)=-1, so there are no H=1 points. Its period is

    integral_R f_n(z) dz=n pi,                         (7.1)

as follows by exp(z/n)=u and the beta integral, or by the elementary
sech integral. The folded kernel is (1/2)sum_(k=0)^(n-1)f_n(z+delta k).
In 0<Im z<2pi it has the pole z=pi i from k=(n-1)/2. Its residue
is -i n/2, and the contour theorem gives n pi exactly.

Inverting the denominator Phi with the audited inversion equation also
writes this example using two positive F_n factors:

    f_n(z)=exp[i pi(2/n-n)/12] exp[-i z^2/(4pi n)]
                   *F_n(z+pi i(n+2))F_n(-z+pi i(n+2)).

Both source heights are (n+2)/2 in (0,n+1). But their central divisors
are 1+t=0 and 1+t^(-1)=0, the same component with opposite v vectors.
Their norm orders cancel. Thus positive factors alone do not suffice;
the coorientation hypothesis in Section 6 has a concrete role.

This boundary contribution can itself be recovered as a regular
generic gluing period. In the positive-pair expression independently
shift the two F_n arguments by alpha and beta. Write a=-exp alpha,
b=-exp beta. The coarse multiplier and its unique generic gluing root are

    H(t)=-(t-b)/(1-a t),    t_*=(1-b)/(a-1).            (7.2)

For small generic shifts, the two source divisors are distinct and
Section 6 cancels them in K_n. In a fixed small circle about z=pi i
there is exactly one remaining pole, at the logarithmic lift of t_*.
On the circle the family is holomorphic in the shifts through their
zero value, where it equals the unshifted K_n. Its Cauchy integral is
therefore a holomorphic germ in
alpha,beta. The generic gluing residue has the regular value -i n/2
at alpha=beta=0, although t_* then lands on the removed divisor t=-1.
Its corresponding period has value n pi. This is an evaluation of a
regular period germ, not a gluing point of the open special fiber.

It illustrates concretely why the comparison object must retain
boundary/nearby-cycle data. The supplied manuscript makes the analogous
distinction in Section 9.4: a boundary character can lose geometric
period data that survive on a space retaining the periods or their
scale. No assertion that the two period problems are equivalent is
being made from that analogy.

Thus a genuine Gaussian--Faddeev type period can have a nonzero
folded source-pole contribution with no gluing solutions. This is not
a counterexample to the volume conjecture or to admissible geometric
states; it disproves an unrestricted inference from quasi-periodicity
to localization solely on H=1. The pole exclusion must be proved for
the chosen state rather than supplied by its boundary algebra.

## 8. The remaining uniform comparison

The selected source realization now has the exact folded period (3.2),
and the algebraic gluing support and local residues are identified.
A finite sum of the residues (5.2) requires proving that this specific
folded cycle is homologous to the corresponding sum of local Leray
cycles, with no remaining polar or infinity contributions. Its integer
coefficients are cycle data, not consequences of Hilbert 90.

The finite recoupling/root descent must additionally match this
relative period, its measure and its transported cycle. Neither the
Koszul equivalence nor the local regulator expression supplies that
identification. The quantum norm comparison with the classical boundary
period, and its all-alternating scope, remain the objective.
