# The exact Weyl-normal insertion for an even threading defect

Private research note, 17 November 2026.

The root even-threading defect vanishes entrywise. Its first normal
before root specialization is therefore a well-defined finite operator
for a prescribed regular lift. This note fixes the genuine integral
Weyl lift and the original source adapters, gives its differentiated-gate
formula, and isolates the divided-power terms in that formula. It does
not assert that the resulting operator or its original closing is
nonzero.

## 1. The prescribed lift and its root value

Fix \(N\ge2\), \(q_0=e^{\pi i/N}\), \(Q=q^2\), and
\[
 \delta(q)=1-q^{2N},\qquad
 \dot A=q\,\frac{dA}{dq},\qquad m=N-1.
 \tag{1}
\]
The core follows the genuine integral Weyl family \(D_m(q)\):
\[
 x=q^{N-1},\qquad M=-q^N.
 \tag{2}
\]
Oppositely oriented legs use its genuine contragredient, not a
generic truncated typical module asserted to remain a Hopf module
off the root wall.

Fix one of the finite open diagrams of the open-threading source,
including its balanced boxes, turns and literal mark, with retained
coupon coefficients regular at the complete point. Fix a relatively
unlinked auxiliary loop \(\gamma\), so \(\ell_S(\gamma)=0\).
Use the original annular polynomial
\[
 C_0=2,\quad C_1=W,\quad C_{n+1}=W C_n-C_{n-1},
 \tag{3}
\]
with \(W=D_1(q)\) and products interpreted as the specified framed
parallel diagrams.

Here is a concrete regular matrix lift of this fixed diagram.
Use the genuine finite Weyl crossing matrices, their inverses, and
genuine dual matrices, in regular bases agreeing with the balanced
root bases. The ordinary Weyl pivotal factor is \(K=q^H\).
To retain the original source factor \(K^{1-N}\), insert its literal
adapter \(K^{-N}\) at each place where that source pivot is prescribed.
Retain the original framing scalars as described in Section 4.
For the marked core, fix \(e_{ab}=1/N\), put \(g(q)=K(q)^{1-N}\),
and prescribe
\[
 \mathsf D(q)=g(q)^{-1}e,\qquad
 \mathsf D_{ab}(q)=\frac{x^{N-1}Q^{-(N-1)a}}{N}.
 \tag{2a}
\]
Define the marked cap by composing the lifted actual cap with
\(\mathsf D(q)\). Thus the associated cut functional is exactly
\(\operatorname{Tr}(g(q)\mathsf D(q)T)=\operatorname{Tr}(eT)\).
At the root, (2a) is the original matrix
\(x^{N-1}Q^a/N\) and the resulting cap is the original marked cap.
Its simplified root entry \(x^a/N^2\) is not used as an independent
off-root formula. Indeed
\[
 \dot{\mathsf D}=(N-1)H\mathsf D,\qquad
                         \frac{d}{dq}(g\mathsf D)=0.
 \tag{2b}
\]
This fixes the marked source jet, not merely its root value.
For a prescribed polynomial Casimir coupon, retain its specified
regular coefficients and replace the generators by these Weyl
matrices. If only a root polynomial is supplied, freeze its coefficients
and use this same polynomial in the generic Casimir. This convention
is part of the lift; no unprescribed meromorphic coupon is used.

Thus all gates and coupons are specified finite holomorphic matrices
near \(q_0\). This is a lift of a fixed source diagram. In particular,
the source-adapted closure is not asserted to be a generic pivotal
functor: \(K^{1-N}\) is not the genuine off-root pivot.

Let \(\mathcal K_\gamma(q)\) and \(\mathcal K(q)\) be these finite
arrays with and without the thread, and put
\[
 \Delta_\gamma(q)=\mathcal K_\gamma(q)-2\mathcal K(q).
 \tag{4}
\]
At \(q=q_0\) the matrices, marks, phases and pivots are exactly the
original source. The entrywise threading theorem gives
\[
                  \Delta_\gamma(q_0)=0.
 \tag{5}
\]
Consequently the following quotient is removable entrywise:
\[
 J_{\gamma,N}
   =\left[\frac{\Delta_\gamma(q)}{\delta(q)}\right]_{q=q_0}
   =-\frac1{2N}\dot\Delta_\gamma(q_0).
 \tag{6}
\]
This defines the first normal of this prescribed lift. It is not a
meridian derivative at fixed \(q_0\).

**Theorem.** For this lift, (6) is given by the full finite
one-differentiated-gate sum of Section 3, with crossing coefficients
(12)--(15), original source adapters (18)--(21), and marked observation
(24). It obeys the exact exterior localization (17).
Neither nonvanishing nor Ward closedness of the normal insertion is
part of the assertion. The following sections prove these statements.

The generic Weyl auxiliary color identity is
\[
             C_{2N}([W])=[D_{2N}]-[D_{2N-2}].
 \tag{7}
\]
It follows from the nonsingular integral exact sequence
\(0\to D_{r+1}\to W\otimes D_r\to D_{r-1}\to0\).
Its actual auxiliary trace is additive, by the same filtration
argument before root specialization. Thus (7) can be used in the
genuine Weyl evaluation. Any source adapters inserted into that
evaluation must also be transported, or differentiated in the original
unfused diagram. One must not differentiate the root-only identity
\(C_{2N}=[\mathbb C_{2N}]+[\mathbb C_{-2N}]\) as if it held off root.
The unfused definition (3)--(4) avoids any such substitution.

## 2. Regular divided matrices and the local crossing coefficient

For every fixed nonnegative highest weight \(a\), use the divided-\(F\)
basis \(v_j\), \(0\le j\le a\), of \(D_a(q)\):
\[
 Kv_j=q^{a-2j}v_j,\quad
 Ev_j=[a-j+1]_qv_{j-1},\quad
 Fv_j=[j+1]_qv_{j+1}.
 \tag{8}
\]
Arrows outside the range are zero. Multiplication of consecutive
entries gives
\[
 E^{(r)}v_j={a-j+r\brack r}_qv_{j-r},\qquad
 F^{(r)}v_j={j+r\brack r}_qv_{j+r},
 \tag{9}
\]
when the target exists, and zero otherwise. These symmetric Gaussian
binomials are Laurent polynomials. For example, conversion to the
ordinary Gaussian polynomial at \(q^2\), followed by its two-term
recurrence, proves polynomiality without evaluating a zero factorial.
Thus (9), and all their ordinary \(q\)-derivatives, are regular at
\(q_0\), even for \(r\ge N\).

For two Weyl colors of highest weights \(a,b\), the unpermuted
genuine crossing is
\[
 R_{a,b}(q)=D(q)\sum_{r=0}^{\min(a,b)}
          c_r(q)\,E_a^{(r)}\otimes F_b^{(r)},\qquad
 D(q)=q^{H_a\otimes H_b/2},
 \tag{10}
\]
on the fixed Cartan half-character cover, where
\[
 c_r(q)=q^{r(r-1)/2}(q-q^{-1})^r[r]_q!
       =q^{r(r-1)/2}\prod_{s=1}^r(q^s-q^{-s}).
 \tag{11}
\]
The genuine finite \(R\) formula gives the first expression; the
second is an exact cancellation of the symmetric factorial.
The nilpotent sum is triangular with diagonal one, so its inverse,
and hence the crossing inverse, is also regular at \(q_0\).
The checked crossing merely includes the fixed tensor flip.

For \(N\le r<2N\), exactly one factor in (11) vanishes at \(q_0\).
Since
\[
 q^N-q^{-N}=-q^{-N}\delta(q),\qquad -q_0^{-N}=1,
\]
one obtains the explicit coefficient
\[
 b_{r,N}:=\left[\frac{c_r(q)}{\delta(q)}\right]_{q=q_0}
   =q_0^{r(r-1)/2}
          \prod_{\substack{1\le s\le r\\s\ne N}}
                         (q_0^s-q_0^{-s}).
 \tag{12}
\]
For \(r\ge2N\), at least two factors vanish, and its first divided
coefficient is zero. In particular,
\[
 b_{N,N}=(-1)^{N-1}N.
 \tag{13}
\]
Indeed \(\prod_{s=1}^{N-1}(q_0^s-q_0^{-s})=i^{N-1}N\) and
\(q_0^{N(N-1)/2}=i^{N-1}\).

Put \(A_r=E_a^{(r)}\otimes F_b^{(r)}\). The complete local derivative is
\[
 \dot R_0=D_0\left[
       \frac{H_a\otimes H_b}{2}\sum_r c_r(q_0)A_r(q_0)
       +\sum_r\{\dot c_r(q_0)A_r(q_0)
                                  +c_r(q_0)\dot A_r(q_0)\}\right].
 \tag{14}
\]
For \(r<N\),
\[
 \dot c_r(q_0)=c_r(q_0)\left[
     \frac{r(r-1)}2+
       \sum_{s=1}^r\frac{s(q_0^s+q_0^{-s})}{q_0^s-q_0^{-s}}
                         \right].
 \tag{15}
\]
For \(N\le r<2N\), \(\dot c_r(q_0)=-2N b_{r,N}\), and the
terms containing \(c_r(q_0)\) vanish. For \(r\ge2N\), both
\(c_r(q_0)\) and \(\dot c_r(q_0)\) vanish.
Equations (12)--(15) include every term, rather than just the
nonzero coefficient (13).

The range of the actual colors matters. If either incident color is
the core \(D_{N-1}\) or the fundamental \(D_1\), the sum in (10) has
no \(r\ge N\) term. In the completely unfused cable all crossings
therefore use only \(r<N\). In the fused representation (7),
the high terms can occur at crossings between two sufficiently large
auxiliary colors, including pieces of an auxiliary self-crossing.
They do not appear at a mixed auxiliary--core crossing merely because
the auxiliary highest weight is \(2N\).

## 3. The full finite gate insertion and exterior localization

Each term of the Chebyshev cable is a finite tensor contraction of
regular gates. Differentiating it gives the sum over all locations of
the contraction with exactly that gate replaced by its derivative.
This follows entrywise from the ordinary finite product rule; there
are no infinite sums or limiting exchanges. Subtract twice the
corresponding unthreaded derivative and multiply by \(-1/(2N)\)
to obtain (6).

Use (14) at a positive crossing and
\[
             \dot R^{-1}_0=-R^{-1}_0\dot R_0R^{-1}_0
 \tag{16}
\]
at a negative crossing. Differentiate the genuine dual matrices,
every retained coupon, the marked lift (2a)--(2b), all scalar phases, and
the source adapters below in the same fixed order. This is the
exact finite operator formula for \(J_{\gamma,N}\).
It is not permission to keep only the terms (12).

There is useful exact localization. If \(\mathcal L(q)\) is any
regular finite exterior contraction, with all its source data, then
\[
 \left[\frac{\mathcal L(q)[\Delta_\gamma(q)]}{\delta(q)}
                                      \right]_{q=q_0}
                     =\mathcal L(q_0)[J_{\gamma,N}].
 \tag{17}
\]
The term differentiating \(\mathcal L\) multiplies (5) and is zero.
The same reasoning applies to regular basis changes:
if \(\Delta'_\gamma=B(q)^{-1}\Delta_\gamma B(q)\), then
\(J'_{\gamma,N}=B(q_0)^{-1}J_{\gamma,N}B(q_0)\).
Thus no derivative of a basis adapter may be omitted from an
individual gate arbitrarily, but all such derivatives telescope in
the complete vanishing defect.

## 4. Source pivot, twist and the two normal directions

On a color \(D_a(q)\), \(K=q^H\). At the root,
\[
 K^{1-N}_0=(-1)^aK_0,\qquad
 \left.\dot K^{1-N}\right|_0
       =(-1)^a\dot K_0-N(-1)^aH K_0.
 \tag{18}
\]
This follows by differentiating \(K^{1-N}=K K^{-N}\) and using
\(K^{-N}_0=(-1)^aI\). Hence changing from the genuine ordinary
pivotal family to the source pivotal family inserts the additional
diagonal weight \(-NH\) at that closure, after its root scalar is
matched. It is not generally a scalar moment.

The genuine highest-weight twist is \(q^{a(a+2)/2}\).
The prescribed source twist has the factor
\(q^{a^2/2+(1-N)a}\). Their ratio and logarithmic derivative are
\[
               q^{-Na},\qquad -Na.
 \tag{19}
\]
For inverse twists the corresponding inverse derivative is retained.
For the original zero-framed \(b\)-strand core knot of writhe
\(\ell\), these local factors give the routewise adapter
\[
 q^{\,N(N-1)(\ell-b+1)+
                         2N\sum_{\text{closed legs}}j}.
 \tag{20}
\]
It is one at the root but its derivative is the displayed
closed-position moment. Equation (20) is the original core adapter;
for auxiliary cablings or other source diagrams use the local
factors (18)--(19) in their actual locations, not an unsupported
reuse of the core formula.

The missing cyclic raising entry of the generic truncated array is
\[
 w(q,M)=M Q^{-N}-M^{-1}
       =\kappa+\frac{M\delta}{1-\delta},
 \qquad \kappa=M-M^{-1}.
 \tag{21}
\]
On (2), \(w\equiv0\). For \(Q=Q_0(1+\epsilon)\), the derivative
along (2) is \(\partial_\epsilon+N\partial_{\log Y}\), with
\(Y=M^2\). This is different from a fixed-meridian root-normal
derivative and from a fixed-root meridian derivative.
The fixed-root threading defect and all its meridian derivatives
vanish; that fact does not determine (6).

## 5. The actual divided-adjoint closing, with its boundary term

After any original exterior contraction in (17), let \(T\) be the
resulting matrix on the marked core. At the root let
\[
 W=E_{N-1,0},\qquad
 \Phi(T)=\operatorname{Tr}(eT),\quad e_{ab}=1/N,
 \qquad
 \Phi_{\rm div}(T)=-\frac{\Phi(J_{\rm ad}(TW))}{N-1}.
 \tag{22}
\]
Here \(J_{\rm ad}\) is the actual divided Hopf adjoint from the
direct source, not commutation by a divided power on the individual
color. Its exact normalization is
\[
 J_{\rm ad}(W)=-N\sum_{j=1}^{N-1}E_{j-1,j},
                 \qquad \Phi_{\rm div}(I)=1.
 \tag{23}
\]
Writing \(\delta_{\rm W}T=([K,T],[F,T])\) and \(h_{\rm W}\) for
the original finite Ward contraction, the all-matrices identity is
\[
 \Phi(T)=
 -\frac{\Phi(J_{\rm ad}(TW))}{N-1}
 -(\Phi_{\rm div}-\Phi)\,
                         h_{\rm W}\delta_{\rm W}T.
 \tag{24}
\]
This is the exact original marked observation of the normal
insertion. The last term is retained. Generic Hopf covariance cannot
be assumed for the source-adapted pivot or the non-Hopf mark.
If independent source data make \(T\) Ward closed, that term
vanishes; it does not vanish merely because \(T\) is a derivative
of a threading defect.

For an ordinary root pivotal partial trace, the first term in (24)
can equivalently be moved before that trace using
\[
 \Phi_{\rm div}(\operatorname{ptr}_g U)=
 -\frac{\Phi\!\left(\operatorname{ptr}_g
          J_{\rm ad,total}[\,U(W_{\rm cut}\otimes I)\,]\right)}
        {N-1}.
 \tag{25}
\]
The order \(U(W_{\rm cut}\otimes I)\) and all mixed Hopf-adjoint
terms are mandatory. This is the direct source's all-matrices
identity, so it applies to the finite insertion sum without
assuming a nonzero or scalar normal coefficient.

## 6. What remains unproved

For an unlinked auxiliary unknot in the genuine pivotal convention,
the virtual dimension is \(q^{2N}+q^{-2N}\). Its value is two
and its first derivative is zero at \(q_0\). Therefore a nonzero
local coefficient in (12) is not evidence of a nonzero full normal.
The source pivot gives instead
\(q^{2N(1-N)}+q^{-2N(1-N)}\), whose first derivative is also zero.
Likewise (23) is a normalization of a marked cochain, not a
nonvanishing theorem for the contraction in (24).

The formulas above compute the first normal exactly once the
specified diagram is supplied. They neither establish universal
first-order vanishing nor exhibit a surviving geometric coefficient.
If the full insertion sum cancels, a higher-order normal must be
computed from the same prescribed family. No equality with a
meridian normal, quantum invariant of a different source, or
geometric period is inferred.

## Complete direct sources

All four texts were read completely at the following pins.

1. [Even threading on the original open marked source](research_open_star_even_threading_scalar.md),
   SHA256 \(\texttt{16ccfefd37d51f96130187ac3a6327552863286dbf35d42b880c9577ab220563}\).
   This supplies the exact entrywise root zero (5).
2. [The actual ADO threaded character](ado_threaded_shadow.md),
   SHA256 \(\texttt{c97b10ee6fa4d629e5f5e21297eec78acf236a7f136628b1153e97b413b6910d}\).
   This supplies the literal annular polynomial and nonsingular
   generic Weyl color identity (7).
3. [Complete-color divided Ward operators and the exact fusion ghost](complete_color_divided_ward_and_fusion.md),
   SHA256 \(\texttt{8add5faf754a4ab5eef78829e0e85b83a0d50c38ed197d20f47a7d84ebfa05cc}\).
   This fixes the genuine Weyl matrices, divided powers, original
   crossing, and the normal and pivotal adapters.
4. [The divided adjoint pairs nontrivially with the actual missing edge](divided_adjoint_marked_edge_pairing.md),
   SHA256 \(\texttt{5b70af4904b257ce8440765608990997aaf5d676f7698c0a4144b2264b03b7a5}\).
   This supplies the all-matrices marked identities (22)--(25).

Only finite written matrix identities and source reads are used.
No mathematical program, numerical experiment, or build was run.
