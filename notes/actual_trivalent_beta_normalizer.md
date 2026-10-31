# Exact normalizer of the original trivalent source

28 October 2026. The central factor of the original balanced trivalent
source is determined exactly. It is not an arbitrary periodic multiplier
or an assumed tame normalization. The proof uses its actual finite
source, the two root shifts, the zero of the full function, and global
analytic rigidity on the central projective line.

With the definitions and logarithmic conventions of
[the exact beta-source theorem](actual_trivalent_quantum_beta_source.md),
put h=2*pi*i/N, Q=exp h and

    phi_N=Psi_+(h)
         =sqrt(N)exp{i*pi[1/4-(N+N^(-1))/12]}.

The exact residue block in that theorem is

    S_N(u,v)=A_N(u) exp[-Log(v/u)Log u/h] Psi_+(Log(v/u)).

Its normalizer is EXACTLY

    A_N(u)=(N/phi_N) u^N Psi_+(h-Log u).               (1)

Consequently the complete original sink polynomial satisfies

    B_N(u,v)=(N/phi_N) u^N
       exp[-Log(v/u)Log u/h]
       Psi_+(Log(v/u))Psi_+(h-Log u)
                 +(1-u^N+v^N) I_N(u,v),                (2)

where I_N is the specified upward convergent Barnes contour in the
beta-source theorem. Its uniform O(1) estimate in the positive boundary
chamber is unchanged. In particular the factor u^N is compulsory and
can have an exponential rate. It is not removed by setting a peripheral
variable to a numerical special value.

## 1. The actual source defines the periodic normalizer

First work away from u=0 and u^N=1. Write u=exp l and choose ANY c_*
with

    exp(N c_*)=1-u^(-N), w=u exp c_*, u^N-w^N=1.

The original finite balanced polynomial defines

    A_N(l)=exp(c_* l/h) B_N(u,w)/Psi_+(c_*).            (3)

Replacing c_* by c_*+h changes w to Qw. The balanced recurrence

    (u-w) B_N(u,Qw)=B_N(u,w)

and the exact full-Psi step show that (3) is unchanged: the combined
ratio is u(1-w/u)/(u-w)=1. Thus no root choice is suppressed in (3).

The simultaneous boundary recurrence of the SAME original polynomial is

    w B_N(Qu,Qw)=(u-1)B_N(u,w)

on the balanced locus. Keep c_* fixed and replace l by l+h in (3).
It follows exactly that

    A_N(l+h)=(1-u^(-1))A_N(l).                        (4)

Psi_+(h-l) has precisely the same step. Therefore

    R_N(l)=A_N(l)/Psi_+(h-l)

has period h and descends to a meromorphic function R_N(z) of

    z=exp(N l)=u^N.                                  (5)

This descent is proved on the logarithmic cover by the exact finite
source recurrences. It is not inferred from only integer samples of
a false constant-monodromy interpolation.

## 2. No finite central poles except the checked collision

Every zero and pole of the original full Psi_+ has exp(N Z)=1.
Indeed its zeros occur at Z=-m h-2*pi*i*n and its poles at
Z=(N+1+m)h+2*pi*i*n, with m,n>=0; coincident points at a rational
root have their actual multiplicities. Only their central location
is needed here.

Alternatively this central-location statement follows from the
independently checked zero-free open fundamental strip and the
exact h shift: all newly introduced zeros or poles come from
1-exp Z and its h translates. No additional global divisor theorem
is required for this proof.

For finite z different from zero and one, the central exponentials
of the two denominator functions in R_N are

    exp(N c_*)=1-z^(-1), exp(N(h-l))=z^(-1).

Neither equals one. The root-independent expression (3) is therefore
holomorphic there. The balanced Fourier recurrence also makes B_N(u,w)
nonzero, although nonvanishing is stronger than needed for the present
pole exclusion. Thus R_N is holomorphic on C minus {0,1}.

At z=1 choose the representative u_0=Q^(-1), l_0=-h. If w tends
to zero on the balanced locus, the first nonzero coefficient is

    B_N(u_0,w)=[NQ/(1-Q)] w+O(w^2).

For example this coefficient follows by differentiating the finite
products, or from their coefficient recurrence and geometric sums.
The constant coefficient vanishes to order z-1 and is smaller than w.
Also c_*=Log(w/u) tends to the left end and Psi_+(c_*) tends to one.
Since exp(c_* l/h) tends to exp(-c_*) up to a factor tending to one,

    A_N -> N/(1-Q).

The exact marked root value is Psi_+(2h)=phi_N/(1-Q). Hence z=1
is removable in R_N and

    R_N(1)=N/phi_N.                                 (6)

This argument also covers N=2, using the logarithmic representative
l_0=-h; no overlap of two open half-plane charts is required.

## 3. At the two ends the normalizer has degree at most one

These are FIXED-N asymptotics used for exact rigidity, not a
semiclassical interchange of N and an end limit.

As z tends to infinity choose

    w=u(1-u^(-N))^(1/N),
    c_*=-z^(-1)/N+O(z^(-2)).

The first Newton factor is u-w=O(u^(1-N)); every subsequent
factor is O(u). Thus all nonconstant terms of B_N(u,w) are O(1/u)
or smaller, and B_N(u,w) tends to one. Moreover exp(c_* l/h)
tends to one. The full function has a simple zero at zero, and its
exact step gives

    Psi_+'(0)=-Psi_+(h)=-phi_N.

Finally Psi_+(h-l) tends to one at the left end. Therefore

    R_N(z)/z -> N/phi_N as z -> infinity.             (7)

At z tending to zero choose w tending to w_0=exp(h/2), for which
w_0^N=-1. Choose l with bounded IMAGINARY part; its real part tends
to minus infinity. Then

    c_*=h/2-l+O(z).

B_N(u,w) remains bounded, since it is a finite polynomial with
u tending to zero and w tending to w_0. Both c_* and h-l tend
to the right end. The EXACT full-Phi horizontal asymptotic is

    Psi_+(Z)=zeta_b exp[-Z^2/(2h)+(N+1)Z/2+pi*i*c_b^2]
                      (1+o(1)), Re Z -> +infinity,      (8)

uniformly on any bounded imaginary strip. It follows from the
independently proved inversion and the left-end asymptotic.
Here c_b=i(sqrt(N)+1/sqrt(N))/2. The bounded error O(z) in c_*
changes the logarithm of (8) by O(z Log z), which tends to zero.

Substitute Z_1=h/2-l and Z_2=h-l in the denominator product of

    R_N=exp(c_* l/h) B_N(u,w)
                    /[Psi_+(c_*)Psi_+(h-l)].

Their logarithms have quadratic/linear part

    -l^2/h+(1/2-N)l+constant,

whereas c_*l/h has part -l^2/h+l/2. The log-squared terms cancel
and the difference is Nl+constant. Thus

    R_N(z)=O(z) as z -> zero.                         (9)

Choosing an Nth-root logarithm of z in any bounded-width strip
makes the estimates uniform in its argument. Periodicity (5) then
removes that root choice. No central factor has been assumed small.

## 4. Rigidity fixes the exact answer

The function R_N(z)/z is holomorphic on the punctured central plane,
extends across z=1 by Section 2, and is bounded at both zero and
infinity by Section 3. It extends to a holomorphic function on P^1
and is constant. Its value is N/phi_N by either (6) or (7).
This proves (1), hence (2), with every original source normalization.

The proof first determines a specific actual period and its divisor
and end behavior. Periodicity alone would allow arbitrary functions
of u^N; the global holomorphy and the two degree bounds are the
extra rigidity that eliminate them.

## 5. The selected two-shape symbol and an actual open source class

Let x=v/u, y=1/u, l=Log u and c=Log x in the positive boundary
chamber. BOTH x and y are upper. The exact shift gives

    Psi_+(h-l)=Psi_+(-l)/(1-y).

The already proved uniform full-Psi strip symbol consequently yields

    S_N(u,v)=(N/phi_N) sqrt[(1-x)/(1-y)]
               exp[W_res(u,v)/h](1+O_K(1/N)),
    W_res=Li_2(x)+Li_2(y)-c*l+2*pi*i*l.                (10)

The roots and logarithms are the selected upper-strip ones. This is
uniform, with every fixed derivative, on ANY compact positive boundary
family, irrespective of the moduli of u,x,y. Its density is explicit
and nonzero. No central periodic amplitude remains unresolved.

For comparison with the finite Newton critical action, the lower
inversion identity implies

    W_res=W_mark+pi^2/3,
    W_mark=Li_2(v/u)-Li_2(u)+l^2/2-l Log v+pi*i*l.

The exact phi_N in (10) is retained. Its leading phase accounts for
the further real -pi^2/6 shift, giving the marked finite-product
critical value W_mark+pi^2/6. No imaginary normalization has been
chosen to manufacture a volume.

In particular, on this entire chamber,

    log|S_N|=N Lambda(u,v)+(1/2)log N+O_K(1),
    Lambda=Im W_res/(2*pi),
    delta_norm=max(0,log|u|,log|v|).                  (11)

If a compact family has Lambda>=delta_norm+eta with eta>0, the
actual source identity (2) and its uniform Barnes bound prove

    B_N(u,v)=S_N(u,v)[1+O_K(N^(-1/2)exp(-N eta))].    (12)

Thus its original geometric residue has coefficient EXACTLY one
and its complete normalization current is exponentially smaller.
This conclusion uses the original relative source and the exact
norm factor, not just nonvanishing of a Hessian or a formal line.
It is uniform for the actual O(1/N) Q-tag shifts in the original
kernel.

This class is genuinely open and nonempty among positive bipyramids.
For |u|=|v|=1, v=1 and Im u<0, the norm rate is zero while

    Lambda(u,1)=-Im Li_2(u)/pi>0.

The strict sign follows by integrating -Arg(1-t u) along 0<t<1.
The two outputs x=y=1/u are upper. The three-side shapes are
p=q=2-u upper and H=u(2-u) lower, so they form a strictly positive
signed bipyramid. Every compact subarc has a strictly positive gap,
which persists in a full open neighborhood of (u,v). The independent
positive Parseval proof in
[the sink-source theorem](actual_sink_source_convolution.md) gives
the same rate on its overlapping |u|<1 chamber.

In particular there is the following genuine volume limit for the
original local polynomial, uniform for theta in compact subsets
of (0,pi):

    lim_(N->infinity) (2*pi/N)log|B_N(exp(-i*theta),1)|
                                         =2 D(exp(i*theta)). (13)

Indeed its gap is positive, the two unit-shape Bloch values equal
their dilogarithm imaginary parts, and the logarithmic cross terms
in (10) are real on this unit boundary. The identical limit holds
with the actual tags B_N(Q^2 exp(-i*theta),Q), by the uniform theorem.
This is a continuum of positive bipyramid fibers with the LITERALLY
original source. It is not asserted to be a family of knot invariants.

This does not eliminate the current outside the gap or the remaining
joint exterior cycle. In particular the positive bipyramid with bounded
local source in Section 7 of the beta-source theorem is fully consistent
with (2). No broad knot theorem follows from this local normalizer.

There is also an independent
[compact Fermat-curve proof](exact_balanced_source_normalizer_fermat.md)
of the same exact normalizer, including its central factor and phase.

The [full-Psi audit](../experiments/audit_actual_trivalent_quantum_beta_source.py)
and [results](../experiments/actual_trivalent_quantum_beta_source_results.json)
check twelve exact normalizers including both |u|<1 and |u|>1,
the original coefficient tags and the independent Barnes source
quadratures. The exact proof above does not infer rigidity from those
finite checks.
