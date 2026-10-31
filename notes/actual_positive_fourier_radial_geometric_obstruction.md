# The radial positive Fourier comparison does not supply a common geometric frame

30 October 2026. The positive coefficient
partition retains the original shared Kirchhoff and Fourier constraints.
Nevertheless its ordinary radial coefficient saddles cannot all assemble
into the complete geometric representation of a certified right-angled
augmented plat. The obstruction is conditional on that proposed assembly;
it is not an exponential gap theorem for the positive partition.

## 1. Actual source and geometric hypotheses

Use the original marked matching source and the positive partition of
[the shared Fourier comparison](actual_matching_graph_positive_fourier_partition.md).
Retain its actual port orders, cup/cap monomials, half-twist phases,
folded channels and exact ordinary channel metric. For the geometric
conclusion assume the literal Morse-prefix and positive right-angled
matching-polyhedron certificate of
[the selected-frame obstruction](actual_right_angled_selected_framing_obstruction.md).
Hyperbolicity alone is not substituted for that certificate.

At matching edge i write

    xi_i=a_i/N, omega_i=w_i/N, rho_i=|omega_i|,
    t_i=d-|w_i|, tau_i=t_i/N, lambda_v=k_v/N.

We discuss strict radial saddles: in the limiting coordinates
1/2<tau_i<1, 0<lambda_v<xi_i, and xi_i>0. The complete support
condition is rho_i<=xi_i. Any assertion about the COMPLETE geometric
representation further requires its endpoint channel xi_i=1/2 at
every crossing disk. A saddle at other channels is not identified
with that complete representation.

The coefficient variational theorem supplies the actual selected
ordinary kernel at

    y_v=log w_v^*,
    nu_v=tau_i/2-i y_v/(2pi),
    Y_v^*=exp[2pi i(lambda_v+1/2-xi_i)].              (1)

Here w_v^*>0 is the coefficient's radial tilt; it is unrelated to
the signed integral matching variable w_i. These are local ordinary
kernel statements, not a claim about completed partner amplitudes.

## 2. Why every radial local factor is central

The central domain of the proved joint packet is

    1/2<Re tau<1, |2Re nu-Re tau|<1/2.              (2)

Every point (1) lies strictly in this domain, since its last expression
is zero. The local source selects its continued characteristic there.

This assertion respects BOTH actual degree adapters. In the low block
the original physical wires are nu and tau-nu, with real parts tau/2.
In the high block they are 1+nu-tau and 1-nu, with real parts
1-tau/2. Thus the high adapter has the same normalized central point;
it is not obtained by applying a low formula to the wrong physical
total degree. Reversing the two physical ports replaces nu by tau-nu
and leaves the central property intact.

It also respects BOTH ends of a matching edge. The actual white map
is the reversed conjugate Clebsch column with its ordinary positive
channel metric. The exact shared-cycle compiler proves that, after
its own endpoint scalar, it uses the SAME normalized finite f as the
black map. The distinct physical input/output momentum conventions
are those of the selected-local certificate; they are not changed
by declaring a new reciprocal branch. Consequently, if these factors
assemble into an actual framed critical representation, every input
and every output has the source-selected central coordinate (2).

It follows immediately from the selected-frame obstruction that:

    No all-ordinary strict radial Fourier reconstruction can assemble
    into the complete positively oriented geometric representation
    in one common actual source frame.                          (3)

The geometric theorem covers the retained half twists and actual
projection prefixes. The contradiction does not use a freely chosen
circle packing or unrelated face labels. In particular adding the
real constrained stationarity equations of the positive partition
cannot make such an assembly possible: (3) already holds before
those extra equations are imposed.

## 3. The exact coefficient phase contains missing coordinate data

This failure is also visible directly in the original finite source.
On physical cycle c write the actual FIRST port at vertex v as

    u_v=epsilon_v x_c+B_v, epsilon_v in {+1,-1},
    b_v=max(0,T_i-d), T_i=d+w_i.

The scalar B_v is the literal propagated affine offset. It is not
reduced modulo N. The exact vertex expansion is

    c_v c_(t_i,a_i) sum_k p_(t_i,a_i,k)
       q^[(d-2a_i+2k)(epsilon_v x_c+B_v-b_v)-t_i k]. (4)

After extracting the x_c character, the k-dependent residual phase
in (4) has the exact successive ratio

    exp{2pi i[(B_v-b_v)/N-t_i/(2N)]}.               (5)

No endpoint scalar, cup monomial or half-twist factor changes (5),
because those factors are independent of this coefficient index k.
Other vertices retain their own coefficient indices. Thus on a fixed
affine sign chamber, the leading logarithmic phase has derivative
with respect to lambda_v equal to

    2pi i delta_v,
    delta_v=(B_v-b_v)/N-tau_i/2.                    (6)

Taking positive moduli deletes exactly this derivative. In contrast,
the positive coefficient action L has derivative L_lambda=-y_v.
The positive constrained lambda equations therefore match the real
radial tilts through cycle multipliers, but do not by themselves
match the real magnetic coordinates.

More explicitly, suppose one tries to reconstruct the same radial
local saddle on the original physical cycle. Write X_c=x_c/N. Its
actual normalized first coordinate must satisfy

    nu_v=epsilon_v X_c+(B_v-b_v)/N.                 (7)

Combining (7) with (1) requires BOTH equations

    epsilon_v Im X_c=-y_v/(2pi),
    epsilon_v Re X_c+delta_v=0.                     (8)

The first is the radial magnitude matching. The second is the real
center matching whose term is retained by (5),(6) and omitted in
the positive envelope. It is not a consequence of Kirchhoff closure.
Equivalently, on the original displayed logarithmic character, if one
introduces a complex multiplier Lambda_c for the cycle's linear
coefficient constraint, the local equation is

    -y_v+2pi i delta_v+epsilon_v Lambda_c=0.         (9)

With Lambda_c=2pi i X_c, (9) gives exactly (8). A real multiplier
for the positive action retains only its real part. All of these
statements concern the original affine lift. Introducing additional
logarithmic characters or changing that lift would be extra data,
not a justification for deleting (5).

## 4. What the retained Fourier constraints do prove

The positive comparison still preserves a genuine phase equation.
Let epsilon_b be the slope of the recorded first coordinate at each
actual cup or restored cap of c. The exact source character is

    m_c=sum_v epsilon_v(d-2a_i+2k_v)
                          +d sum_b epsilon_b.

The actual even-cycle proof makes
E_c=sum_v epsilon_v+sum_b epsilon_b even. Fourier extraction requires
m_c=2b_c modulo 2N, where b_c is one at the original marked cycle
and zero elsewhere. Substitution of (1), using d=N-1, gives EXACTLY

    product_v (Y_v^*)^epsilon_v (-1)^(sum_b epsilon_b)
          =Q^(E_c/2+b_c).                          (10)

Thus the cup signs, finite pivotal correction and original one-unit
charge remain specified. Their limiting product is one. Equation
(10) closes these particular phase characters on the actual physical
cycles; it does not supply (8), a common geometric frame, all complex
edge equations, or a contributing source integration cycle.

For reference, the interior positive action with its original scalar is

    S=sum_i [ b(xi_i,rho_i)
                   +L(1-rho_i,xi_i,lambda_(i,W))
                   +L(1-rho_i,xi_i,lambda_(i,pi)) ],
    b(xi,rho)=J(xi+rho)-2J(xi)-2J(rho)-J(xi-rho).   (11)

Here S is the rate of the UNSQUARED coefficient weight; each summand
of Z_F has rate 2S. This follows directly from the exact B_N in the
positive partition and the uniform sine-factorial estimate. Its variables still satisfy
the shared Kirchhoff equations and one fixed Fourier winding branch.
Equation (11) is a local interior rate, not a global Laplace theorem
covering its boundary. In particular no Casson--Rivin identification
of (11) is obtained by differentiating it and ignoring (6).

## 5. Scope and the retained route

This obstruction does NOT prove a strict numerical rate gap between
the positive partition and the original source. Boundary maximizing
sequences, different coherent regroupings, nonradial saddles and
cancellations remain separate questions. It does not rule out a
volume identity whose numerical value is obtained in another way.

The existing [selected-factor localization](actual_augmented_plat_selected_factor_localization.md)
instead puts every ordinary factor outside ONE prescribed matching
edge on its actual selected FULL physical packet. Those coordinates
need not be central or radial. The two exceptional factors are kept
in their exact marked four-port block, with every target and required
generic normal retained. The present calculation preserves that route;
it does not replace its remaining contraction and period estimates.

Focused audit: [finite phase derivatives and adapter identities](../experiments/audit_actual_positive_fourier_radial_geometric_obstruction.py).

The radial obstruction does not give a rate gap or a boundary conclusion.

The common-frame hypothesis and exceptional-block route remain essential.