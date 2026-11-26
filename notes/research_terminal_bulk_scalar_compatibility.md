# Scalar compatibility of the actual terminal source on the physical bulk

Private written proof, 16 November 2026.

For each fixed signed terminal power of magnitude at least two, the
original values and first spectral normals admit one holomorphic scalar
representative with polynomial normalized amplitude on every fixed
physical bulk interval. The proof uses the actual scalar terminal
equation and the known scalar source near complete output. The normal
channel is retained independently until its difference from the
derivative of a value interpolant has been estimated.

The stable part is controlled forward from a retained left buffer.
Only the slow part is transported backward from the right seed. This
distinction is essential. No continuation to a prescribed parent
height, endpoint estimate, or nonzero global closing follows.

## 1. Original source, phases and statement

Fix an integer \(|n|\ge2\), put \(h=N^{-1}\), and retain
\[
 q=e^{\pi i/N},\quad c_0=q+q^{-1},\quad
 P_N(Z)=2T_N(Z/2)+2,\quad
 \eta=(-1)^{N-1},\quad \kappa=q^{(N-1)^2/2}.
\]
Here \(T_N\) is Chebyshev's polynomial; the original turn is \(T\).
In the full physical algebra use
\[
 G_N(Z)=T(R^n)(Z),\qquad
 D_{-n}=\kappa^{-n}TR^nT\,C\,\kappa^nTR^{-n}T.
 \tag{1}
\]
All canonical polynomials and first normals are the original ones.
Let \(\widetilde D_{-n}\) denote the ordinary finite-shift lift.
The exact bivariate residual source gives
\[
 (\widetilde D_{-n}-c_0)G_N
       =(-1)^n\frac{\eta\kappa^n}{N^2}P_N(Z).
 \tag{2}
\]
The right side is retained; the equation is not homogeneous off-grid.

Use the centered row coordinate
\[
 x_j=(j+\tfrac12)h,\quad c(x)=2\cos(2\pi x),\quad
 t(x)=\pi-2\pi x,\quad
 {\cal S}(x)=S_n(t(x)),\quad p(x)=(\sin2\pi x)^{-1/2},
 \qquad f_h(x)=p(x)e^{{\cal S}(x)/h}.
 \tag{3}
\]
The square root is positive on the real bulk. The signed stationary
phase \(S_n\), including its additive constant, is the one in the
characteristic-action and regular-amplitude sources. In particular
\[
       e^{{\cal S}'(x)}=\tau_{\max,-n}(x).
 \tag{4}
\]
This is the dominant root of the literal \(D_{-n}\) equation.
All functions in (3) are holomorphic on sufficiently thin fixed tubes
over any compact subinterval of \((0,1/2)\), and \(p\) is a unit there.

For the two original nodal channels set
\[
 a_j=f_h(x_j)^{-1}G_N(c(x_j)),
\]
\[
 b_j=f_h(x_j)^{-1}c'(x_j)G_N'(c(x_j))
              -\left(\frac{{\cal S}'(x_j)}h+
                              \frac{p'(x_j)}{p(x_j)}\right)a_j.
 \tag{5}
\]
Thus \(b_j\) is the actual first normal after the exact phase and
scalar-gauge correction. In the row transfer its scaled coordinate
is \(h b_j\). Equation (5) does not identify it with the derivative
of a chosen interpolation of \(a_j\).

**Theorem.** For every \(I=[a,b]\Subset(0,1/2)\), there are constants
\(r,c,C>0\), an integer \(p_0\), and \(N_0\), depending on \(n,I\),
such that the following hold for both parities and \(N\ge N_0\).
There is a holomorphic scalar \({\cal A}_N\) on
\[
       \{a-r<\Re x<b+r,\ |\Im x|<r\}
\]
with
\[
 \|{\cal A}_N\|\le C N^{p_0},\qquad
 {\cal A}_N(x_j)=a_j,\qquad {\cal A}_N'(x_j)=b_j
                            \quad(x_j\in I).
 \tag{6}
\]
Consequently \({\cal H}_N(x)=f_h(x){\cal A}_N(x)\) matches the
actual value and first spectral normal of \(G_N\) at every such row:
\[
 {\cal H}_N(x_j)=G_N(c(x_j)),\qquad
 \frac{{\cal H}_N'(x_j)}{c'(x_j)}=G_N'(c(x_j)).
 \tag{7}
\]
The denominator is a unit on this fixed bulk interval. Moreover one
can first construct an exact value interpolant \(A_N\), polynomially
bounded on a slightly larger fixed tube, for which
\[
 \max_{x_j\in I}|b_j-A_N'(x_j)|\le C e^{-cN},\qquad
              \|{\cal A}_N-A_N\|\le C e^{-cN}.
 \tag{8}
\]
Fixed derivatives satisfy the corresponding bounds on smaller tubes.
The exponent \(p_0\) and the available width need not be uniform as
the interval approaches either endpoint or as \(|n|\) increases.

## 2. Scalar specialization and forced-error transport

Define the ordinary normalized scalar operator
\[
 {\mathsf P}_h=f_h^{-1}(\widetilde D_{-n}-c_0)f_h
       =\sum_{k=-m}^m a_{k,h}(x)E^k,
       \qquad m=|n|,\quad E u(x)=u(x+h).
 \tag{9}
\]
On fixed buffered bulk tubes its coefficients, fixed derivatives,
and inverses of the two extreme coefficients are uniformly bounded.
This follows from the original ordinary rows and
\(({\cal S}(x+kh)-{\cal S}(x))/h=O(1)\) for each fixed shift.
Its principal companion has exactly one unit root, of multiplicity
two, with all other roots strictly inside the unit circle. Here and
below a double root retains its two-dimensional generalized space.

We spell out the scalar specialization of the regular-amplitude
proof. Its exact even midpoint coefficients give
\[
                         {\mathsf P}_h1=O_{\rm hol}(h^2).
 \tag{10}
\]
For the scalar companion \(M_h\), let \({\bf r}\) have every entry
one and let \({\bf v}\) consist of its successive integer offsets.
Then
\[
 M_h{\bf r}={\bf r}+O(h^2),\qquad
 M_0{\bf r}={\bf r},\qquad M_0{\bf v}={\bf v}+{\bf r}.
 \tag{11}
\]
The Riesz splitting with these fixed slow columns, the analytic
graph, and the improved first-column estimate of that proof apply
with one scalar channel and no recovery equation. In detail, its
bounded graph \(R_h=O(h)\) has exponential invariance error; (11)
and the graph equation give \(R_h{\bf r}=O(h^2)\). In the two slow
coordinates the matrix is therefore
\[
 \begin{pmatrix}1+O(h^2)&1+O(h)\\O(h^2)&1+O(h)\end{pmatrix}.
\]
The gauge \(\operatorname{diag}(1,h)\) gives a holomorphic transfer
\[
                         T_h=I_2+hB_h,\qquad \|B_h\|\le C.
 \tag{12}
\]
Its embedding and left inverse have polynomial conditioning. The
stable complement has a uniformly exponentially contracting
propagator along the real grid. All these conclusions hold on
fixed smaller tubes, with exponential graph error and derivatives.

For clarity this argument uses neither the \(6^r\) gauged input
system nor its recovery blocks: the present source has the exact
scalar equation (2). The scalar proof above is precisely the
one-channel portion of the regular-amplitude construction, since
its even-symbol and graph-column arguments were proved first for
\(\widetilde D_{-n}-c_0\).

The independent normal companion is the exact prolongation
\[
       \begin{pmatrix}M_h&0\\hM_h'&M_h\end{pmatrix}.
 \tag{13}
\]
If \(G_h\) embeds (12), its slow embedding and transfer are
\[
 \begin{pmatrix}G_h&0\\hG_h'&G_h\end{pmatrix},\qquad
 \begin{pmatrix}T_h&0\\hT_h'&T_h\end{pmatrix}=I_4+O(h).
 \tag{14}
\]
This is rank four, with both normal coordinates independent. The
phase subtraction in (5) is exactly what makes (13) the correct
standard prolongation.

We shall also use the following forced version of this transport.
Suppose a scalar or prolonged packet satisfies its exact recurrence
with error at most \(\varepsilon_N\) per step, and is bounded by
\(M_N\) on a larger real interval. After any fixed positive left
buffer, its distance from the slow graph is at most
\[
 C h^{-p}\varepsilon_N+C e^{-c/h}M_N.
 \tag{15}
\]
On the remaining interval its slow coordinates have forward and
backward propagation bounded by a constant, with total additive
error at most
\[
 C h^{-p}\varepsilon_N+C e^{-c/h}M_N
 \tag{16}
\]
after increasing the fixed exponent \(p\).

Here is the error argument. In the bounded graph frame, before the
polynomial slow gauge, the transverse recurrence is a stable
recurrence forced by the supplied error and the exponential graph
residual times the actual packet. A fixed block of its propagator
is a strict contraction, uniformly along the real interval.
Summing the resulting geometric series proves (15), with the
homogeneous term retaining the original left packet. Polynomial
coordinate changes account for \(h^{-p}\). After that left buffer,
the slow recurrence has transfer (12), or (14), and forcing bounded
by (15) and the original error. Both the transfer and its inverse
have norm at most \(1+Ch\); summing over \(O(h^{-1})\) steps gives
(16). At no point is a stable component propagated backward from
a right-hand value. In particular an exponentially small forcing,
a polynomial or \(e^{o(N)}\) total budget, and an exponentially
small right slow packet give an exponentially small packet on a
fixed inner interval, after the left-buffer term has been included.

## 3. The actual right seed and polynomial bulk packets

The complete terminal source theorem supplies a fixed disk around
external angle \(t=0\) on which the actual ordinary source is
\[
 G_N(-2\cos t)=\epsilon_{n,N}A_n(t)e^{NS_n(t)}
                                  (1+O_n(N^{-1})),
                   \qquad |\epsilon_{n,N}|=1.
 \tag{17}
\]
The error is holomorphic on a slightly smaller disk, and the
amplitude is holomorphic there. The stationary-action calibration
identifies the phase with (3). The known extra unit exponential
scalar at powers \(\pm2\) remains in \(\epsilon_{n,N}\); no finite
carrier is changed by this identification. Negative powers use
the original reflected phase and crossing.

Choose a fixed small \(t_*>0\) in this disk and set
\(x_*=1/2-t_*/(2\pi)\). For a given target \(I\), it can be chosen
to the right of \(I\). A fixed small complex neighborhood of
\(x_*\) lies both in the seed disk and strictly inside the bulk.
On that neighborhood
\[
             g_N^{\rm seed}(x)=f_h(x)^{-1}G_N(c(x))
 \tag{18}
\]
and all its fixed derivatives are polynomially bounded (indeed
bounded after a harmless change of constants in (17)). It is an
actual scalar function, so its derivative gives the actual normal
data (5) there.

Choose several nested fixed real bulk intervals containing both
\(I\) and a closed seed interval about \(x_*\). Their left endpoints
are strictly to the left of \(I\), with positive gaps, and their
right endpoints remain below \(1/2\). These finitely many buffers
will accommodate the two forward-attraction arguments, the finite
shift range, and the interpolation estimates. All complex tubes
are chosen inside the corresponding larger ones.

The actual prefix estimate used in the regular-amplitude source
gives the budget \(e^{o(N)}\) for the normalized terminal value and
scaled normal packets on the largest real buffer. The empty input
is included literally by \(K_N(c_0,Z)=1\), or \(\alpha=i\pi\), so
this is the actual source budget, not a bound on arbitrary solutions.
Equation (2) gives the exact homogeneous value and prolonged normal
recurrences at all these physical rows: \(P_N(c(x))=4\cos^2(\pi Nx)\)
has a double zero at every \(x_j\).

Apply (15) first, with zero supplied recurrence error, to this actual
rank-four packet. After a fixed left buffer its stable part is
exponentially small. At the right seed the remaining packet is
polynomial by (18). The backward slow estimate (16), and its
forward counterpart, now give
\[
       |a_j|+|b_j|+\text{all fixed packet slots}
                                      \le C h^{-p}
 \tag{19}
\]
on the next inner interval. Passing from \(h b_j\) to \(b_j\)
only changes the polynomial exponent. This is the global polynomial
bound needed before testing the derivative defect. The original
left packet was absorbed by forward attraction, not declared zero.

## 4. One exact moderate value interpolant

Consider the value part of the actual scalar packet on this inner
interval. Its regular slow coordinates differ, by an exponentially
small amount, from an exact solution \(z_j\) of (12). To see this,
match one slow packet at an interior row and propagate (12) in both
directions. The actual slow recurrence has exponentially small error
by (15), and the bounded propagators in (12) sum this error over
\(O(N)\) steps. The resulting exact trajectory has polynomial norm.

Apply the analytic near-identity interpolation theorem to \(z_j\).
The grid is translated by \(h/2\), which changes none of its constants.
It gives a holomorphic vector \(Z_N(x)\), polynomially bounded on a
fixed tube, with \(Z_N(x_j)=z_j\). Multiplication by the holomorphic
slow embedding and extraction of the current value slot produce a
polynomially bounded scalar \(A_N^0(x)\) whose errors at the actual
values \(a_j\) are exponentially small.

Repair these errors on a fixed intermediate interval by
\[
 A_N(x)=A_N^0(x)+
       \sum_j\bigl(a_j-A_N^0(x_j)\bigr)
                    \operatorname{sinc}\bigl((x-x_j)/h\bigr).
 \tag{20}
\]
The sum ranges over all its grid points, including the fixed real
buffers that will be used next. Since
\(\operatorname{sinc}z=\int_{-1/2}^{1/2}e^{2\pi izs}ds\),
the correction is bounded by
\(C N^p e^{-cN+\pi N|\Im x|}\). On a sufficiently narrow fixed
tube it and its fixed derivatives are exponentially small. Thus
\[
                A_N(x_j)=a_j,\qquad \|A_N\|\le C N^p.
 \tag{21}
\]
No claim that \(A_N\) solves an exact off-grid equation has been made.

Set
\[
                         r_N(x)={\mathsf P}_h A_N(x).
 \tag{22}
\]
The bounded analytic coefficients and finite shifts in (9) make
\(r_N\) polynomially bounded on a smaller fixed tube. At every
grid point whose shifts remain in (21), the actual value recurrence
gives \(r_N(x_j)=0\).

We use the elementary dense-zero estimate explicitly. In a fixed
disk inside the tube, a real central segment contains \(c/h\) grid
zeros. On a smaller concentric disk the corresponding disk
Blaschke factors have moduli at most a fixed \(q<1\). Dividing by
their product and applying the maximum principle bounds a
polynomially bounded holomorphic function there by
\(C h^{-p}q^{c/h}\). A finite cover of an inner interval, followed
by Cauchy estimates on reserved disks, therefore gives
\[
                 \|r_N\|+\|r_N'\|\le C e^{-c_1N}
 \tag{23}
\]
on a fixed smaller tube. This is the same zeros estimate proved in
the interpolation source; it uses a real buffer on both ends.

## 5. The actual normal defect and its right seed

Let \({\mathsf P}_h^{[1]}=\sum_k a_{k,h}'(x)E^k\), with only
the coefficient differentiated. The original full-normal equation,
after the exact gauge (5), is
\[
        ({\mathsf P}_h b)(x_j)
               +({\mathsf P}_h^{[1]}a)(x_j)=0.
 \tag{24}
\]
One can obtain it by differentiating (2) before specializing to
the physical row. Both the residual and its first derivative
vanish there. Differentiating the local scalar gauge is essential;
without the \({\cal S}'/h+p'/p\) term in (5), (24) would be false.

Differentiating (22) gives the ordinary identity
\[
            r_N'={\mathsf P}_h A_N'
                              +{\mathsf P}_h^{[1]}A_N.
\]
Since (21) matches every shifted value in the row, subtraction
from (24) proves the exact forced defect equation
\[
 d_j=b_j-A_N'(x_j),\qquad
                 ({\mathsf P}_h d)(x_j)=-r_N'(x_j).
 \tag{25}
\]
There is no coefficient-derivative source left over. This is the
source-specific relation that a mere upper profile would not give.
By (19), (21) and Cauchy estimates, the entire defect packet has
polynomial norm on the real buffered interval.

On the right seed, \(A_N-g_N^{\rm seed}\) is a difference of two
polynomially bounded holomorphic functions. They have the same
values at all seed grid points. The dense-zero estimate and Cauchy
therefore make their first derivatives exponentially close on a
smaller seed interval. By (18), this says
\[
                       |d_j|\le C e^{-c_2N}
 \tag{26}
\]
through a fixed right seed packet.

Apply the forced estimate (15) to the scalar defect companion of
(25), using its polynomial global budget and the exponentially
small forcing (23). After another fixed positive left buffer its
stable part is exponentially small. Its right slow packet is
exponentially small by (26) and the polynomially conditioned
projection. Formula (16) then propagates that slow estimate
backward through the entire target interval. Thus
\[
                   \max_{x_j\in I_1}|d_j|\le C e^{-c_3N}
 \tag{27}
\]
on a fixed interval \(I_1\) containing \(I\) in its interior.
All exponents remain positive after taking minima and absorbing
the finitely many polynomial losses. The stable part in this
argument was again bounded from the left, not inverted from (26).

## 6. Exact derivative repair and source consequences

Define, using the rows in \(I_1\),
\[
 {\cal A}_N(x)=A_N(x)+
       \sum_{x_j\in I_1}d_j(x-x_j)
                   \operatorname{sinc}^2\bigl((x-x_j)/h\bigr).
 \tag{28}
\]
At every included row the correction has value zero and derivative
\(d_j\). All other summands have double zeros there. This proves
the exact identities (6). The integral bound for sinc gives a
bound \(C N^p e^{-c_3N+2\pi N|\Im x|}\) for (28)'s correction
on any fixed bounded rectangle. Choose its final width less than
\(c_3/(8\pi)\), and reserve a smaller tube for derivatives.
Then (8) holds. Multiplication by \(f_h\) and the chain rule (5)
prove (7), completing the theorem.

The conclusion has two direct source consequences.

First fix a nonnegative integer \(b\), independent of \(N\), and
the physical endpoint \(w=c_b=2\cos((2b+1)\pi/N)\). The literal
row \(F_{b,N}(Z)=K_N(c_b,Z)\) is an ordinary polynomial of degree
at most \(b\): all higher Newton coefficients vanish. The exact
turn identity gives
\[
 T(R^nK_N(c_b,\cdot))=F_{b,N}(J)G_N.
 \tag{29}
\]
Apply the ordinary finite-shift lift \(F_{b,N}(\widetilde J)\)
to \({\cal H}_N\) on a buffered tube. At each inner physical row
it matches the value and normal of (29), since all shifted values
and normals in that operator are matched in (7). Its normalized
amplitude is polynomially bounded: the finitely many shift ratios
of \(f_h\) and the bulk row coefficients are bounded, and the
ordinary coefficients of \(F_{b,N}\) grow at most polynomially
in \(N\) for each fixed \(b\), directly from its finite Newton
products with indices at most \(b\). The polynomial exponent is
allowed to depend on \(b\). There is no estimate uniform in a
growing mark \(b\), and no conclusion for generic bounded \(\alpha\)
from sampling these marks.

Second, for a fixed finite collection of signed powers and fixed
marks, multiply their scalar representatives at a shared color.
The product has the exact original values and the full shared
normal product rule. Its phase is the sum of their specified
phases, and its normalized amplitude is polynomial on a common
fixed smaller tube. Any original crossing, joint spectator and
remaining trace may stay outside this exact substitution. Thus
on a bulk window the usual original double-pole trace kernel may
use this single scalar amplitude; it introduces no separate
derivative-mismatch interface. The genuine exterior window
boundaries, original aliases and any omitted endpoint rows remain.

Neither consequence identifies this representative with the
canonical polynomial at arbitrary complex free colors. The theorem
does not reach the physical endpoints, provide a whole-period
representative, control prescribed parent heights, or give a lower
bound for the original coherent closing. It removes the independent
bulk scalar-compatibility issue for these actual terminal sources,
without asserting it for arbitrary microscopic endpoint parameters
or the general endpoint-product leaf.

## 7. Coverage and complete direct sources

The near-complete scalar terminal seed, the scalar even-symbol
cancellation, and the analytic near-identity interpolation are
prior results. The added argument is the exact source defect
equation (25), together with forward stable attraction and backward
polynomial slow transport from that genuine seed. It yields the
full-normal scalar representative on any fixed physical bulk.

The following complete sources were freshly read or retained from
their unchanged complete readbacks; their used implications and
all hashes were checked.

* [Regular source amplitude transport](research_filled_leaf_regular_amplitude_transport.md),
  SHA256 7110294071ac8ad878cf3848e744966ab9682c9c29177878842bf94ff6d63574:
  actual prefix budget, signed phase convention, even midpoint
  cancellation, analytic slow graph and polynomial gauge, stable
  attraction, and the independent normal prolongation.
* [Analytic near-identity interpolation](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe:
  complete local interpolation/gluing/repair proof and its dense-zero
  estimate. Only its general matrix interpolation theorem is used.
* [Actual terminal scalar seed](research_uniform_terminal_family_and_star_fillings.md),
  SHA256 d9da305e1567393f5f714f11bd646cd2dca37b7d7569b9ab12d6a63014ece4f9:
  the full holomorphic original terminal expansion for each fixed
  signed power, including its original unit carrier and normals.
* [Signed stationary action calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd:
  the selected original phase and its additive constant, negative
  power reflection, and the power-two calibration.
* [Exact ordinary bivariate residual](research_filled_leaf_exact_bivariate_residual.md),
  SHA256 586cb460d8056f1a0e9df6c1c1be28ee8cbbcf7cf7ae631158722096f0c24dbb:
  the ordinary terminal residual (2) and its full-jet scope.

Only written mathematics, source-text reads and file hashes were
used. No mathematical programs, numerical experiments, tests or
builds were run. Adopted notes and public manuscripts are unchanged.
